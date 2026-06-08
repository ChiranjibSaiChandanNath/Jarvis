"""
JARVIS Action Executor — AppleScript-based system actions.

Execute actions IMMEDIATELY, before generating any LLM response.
Each function returns {"success": bool, "confirmation": str}.
"""

import asyncio
import logging
import os
import re
import time
from pathlib import Path
from urllib.parse import quote

log = logging.getLogger("jarvis.actions")

DESKTOP_PATH = Path.home() / "Desktop"

_SKIP_PERMISSIONS = os.getenv("JARVIS_SKIP_PERMISSIONS", "true").lower() not in ("0", "false", "no")


async def _mark_terminal_as_jarvis(revert_after: float = 5.0):
    """Temporarily set the front Terminal window to Ocean theme, then revert.

    Shows the user JARVIS is active in that terminal. Reverts after revert_after seconds.
    """
    # Save the current profile, switch to Ocean, then revert
    script_save = (
        'tell application "Terminal"\n'
        '    return name of current settings of front window\n'
        'end tell'
    )
    try:
        proc = await asyncio.create_subprocess_exec(
            "osascript", "-e", script_save,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await proc.communicate()
        original_profile = stdout.decode().strip()

        # Switch to Ocean
        script_set = (
            'tell application "Terminal"\n'
            '    set current settings of front window to settings set "Ocean"\n'
            'end tell'
        )
        proc2 = await asyncio.create_subprocess_exec(
            "osascript", "-e", script_set,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await proc2.communicate()

        # Schedule revert
        if original_profile and original_profile != "Ocean":
            asyncio.get_event_loop().call_later(
                revert_after,
                lambda: asyncio.ensure_future(_revert_terminal_theme(original_profile))
            )
    except Exception:
        pass


async def _revert_terminal_theme(profile_name: str):
    """Revert a Terminal window back to its original profile."""
    escaped = profile_name.replace('"', '\\"')
    script = (
        'tell application "Terminal"\n'
        f'    set current settings of front window to settings set "{escaped}"\n'
        'end tell'
    )
    try:
        proc = await asyncio.create_subprocess_exec(
            "osascript", "-e", script,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await proc.communicate()
    except Exception:
        pass


def applescript_escape(s: str) -> str:
    """Escape a string for safe embedding in an AppleScript double-quoted string."""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\r", "").replace("\n", " ")


async def open_terminal(command: str = "") -> dict:
    """Open terminal console window and optionally run a command."""
    import sys
    if sys.platform != "darwin":
        if sys.platform == "win32":
            import subprocess
            success = False
            try:
                if command:
                    subprocess.Popen(["cmd.exe", "/k", command], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    subprocess.Popen(["cmd.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE)
                success = True
            except Exception as e:
                log.error(f"Failed to open terminal on Windows: {e}")
            return {
                "success": success,
                "confirmation": "Terminal is open, sir." if success else "I had trouble opening Terminal, sir.",
            }
        return {"success": False, "confirmation": "Terminal action is not supported on this platform, sir."}

    if command:
        escaped = applescript_escape(command)
        script = (
            'tell application "Terminal"\n'
            "    activate\n"
            f'    do script "{escaped}"\n'
            "end tell"
        )
    else:
        script = (
            'tell application "Terminal"\n'
            "    activate\n"
            "end tell"
        )
    proc = await asyncio.create_subprocess_exec(
        "osascript", "-e", script,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    _, stderr = await proc.communicate()
    success = proc.returncode == 0
    if not success:
        log.error(f"open_terminal failed: {stderr.decode()}")
    else:
        await _mark_terminal_as_jarvis()
    return {
        "success": success,
        "confirmation": "Terminal is open, sir." if success else "I had trouble opening Terminal, sir.",
    }


async def open_browser(url: str, browser: str = "chrome") -> dict:
    """Open URL in user's browser (Chrome or Firefox)."""
    import sys
    if sys.platform != "darwin":
        import webbrowser
        success = False
        try:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, lambda: webbrowser.open(url))
            success = True
        except Exception as e:
            log.error(f"Failed to open browser on Windows/Linux: {e}")
        return {
            "success": success,
            "confirmation": f"Pulled that up in browser, sir." if success else "I had trouble opening the browser, sir.",
        }

    escaped_url = url.replace('"', '\\"')

    if browser.lower() == "firefox":
        app_name = "Firefox"
        script = (
            'tell application "Firefox"\n'
            "    activate\n"
            f'    open location "{escaped_url}"\n'
            "end tell"
        )
    else:
        app_name = "Chrome"
        script = (
            'tell application "Google Chrome"\n'
            "    activate\n"
            f'    open location "{escaped_url}"\n'
            "end tell"
        )

    proc = await asyncio.create_subprocess_exec(
        "osascript", "-e", script,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    _, stderr = await proc.communicate()
    success = proc.returncode == 0
    if not success:
        log.error(f"open_browser ({app_name}) failed: {stderr.decode()}")
    return {
        "success": success,
        "confirmation": f"Pulled that up in {app_name}, sir." if success else f"{app_name} ran into a problem, sir.",
    }


# Keep backward compat
async def open_chrome(url: str) -> dict:
    return await open_browser(url, "chrome")


async def open_claude_in_project(project_dir: str, prompt: str) -> dict:
    """Open Terminal, cd to project dir, run Claude Code interactively."""
    claude_md = Path(project_dir) / "CLAUDE.md"
    claude_md.write_text(f"# Task\n\n{prompt}\n\nBuild this completely. If web app, make index.html work standalone.\n")

    import sys
    if sys.platform != "darwin":
        if sys.platform == "win32":
            import subprocess
            success = False
            try:
                skip_flag = " --dangerously-skip-permissions" if _SKIP_PERMISSIONS else ""
                cmd = f'cd /d "{project_dir}" && claude{skip_flag}'
                subprocess.Popen(["cmd.exe", "/k", cmd], creationflags=subprocess.CREATE_NEW_CONSOLE)
                success = True
            except Exception as e:
                log.error(f"Failed to open Claude on Windows: {e}")
            return {
                "success": success,
                "confirmation": "Claude Code is running in a new Command Prompt window, sir."
                if success
                else "Had trouble spawning Claude Code, sir.",
            }
        return {"success": False, "confirmation": "Spawning Claude Code in project is not supported on this platform, sir."}

    skip_flag = " --dangerously-skip-permissions" if _SKIP_PERMISSIONS else ""
    escaped_dir = applescript_escape(project_dir)
    script = (
        'tell application "Terminal"\n'
        "    activate\n"
        f'    do script "cd {escaped_dir} && claude{skip_flag}"\n'
        "end tell"
    )
    proc = await asyncio.create_subprocess_exec(
        "osascript", "-e", script,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    _, stderr = await proc.communicate()
    success = proc.returncode == 0
    if not success:
        log.error(f"open_claude_in_project failed: {stderr.decode()}")
    else:
        await _mark_terminal_as_jarvis()
    return {
        "success": success,
        "confirmation": "Claude Code is running in Terminal, sir. You can watch the progress."
        if success
        else "Had trouble spawning Claude Code, sir.",
    }


async def prompt_existing_terminal(project_name: str, prompt: str) -> dict:
    """Find a Terminal window matching a project name and type a prompt into it.

    Uses System Events keystroke to type into an active Claude Code session
    rather than `do script` which would open a new shell.
    """
    import sys
    if sys.platform != "darwin":
        return {
            "success": False,
            "confirmation": "Prompting an existing terminal is only supported on macOS, sir.",
        }

    escaped_name = applescript_escape(project_name)
    escaped_prompt = applescript_escape(prompt)

    # Single atomic script: find window, focus it, type into it
    script = f'''
tell application "Terminal"
    set matched to false
    set targetWindow to missing value
    repeat with w in windows
        if name of w contains "{escaped_name}" then
            set targetWindow to w
            set matched to true
            exit repeat
        end if
    end repeat

    if not matched then
        return "NOT_FOUND"
    end if

    -- Bring the matched window to front
    set index of targetWindow to 1
    set selected tab of targetWindow to selected tab of targetWindow
    activate
end tell

-- Wait for window to be fully focused
delay 1

-- Now type into it
tell application "System Events"
    tell process "Terminal"
        set frontmost to true
        delay 0.3
        keystroke "{escaped_prompt}"
        delay 0.2
        keystroke return
    end tell
end tell

return "OK"
'''

    try:
        proc = await asyncio.create_subprocess_exec(
            "osascript", "-e", script,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=15)

        result = stdout.decode().strip()
        if result == "NOT_FOUND":
            return {
                "success": False,
                "confirmation": f"Couldn't find a terminal for {project_name}, sir.",
            }

        success = proc.returncode == 0
        if not success:
            log.error(f"prompt_existing_terminal failed: {stderr.decode()[:200]}")

        if success:
            await _mark_terminal_as_jarvis()

        return {
            "success": success,
            "confirmation": f"Sent that to {project_name}, sir." if success
            else f"Had trouble typing into {project_name}, sir.",
        }

    except asyncio.TimeoutError:
        return {"success": False, "confirmation": "Terminal operation timed out, sir."}
    except Exception as e:
        log.error(f"prompt_existing_terminal failed: {e}")
        return {"success": False, "confirmation": "Something went wrong reaching that terminal, sir."}


async def get_chrome_tab_info() -> dict:
    """Read the current Chrome tab's title and URL via AppleScript."""
    import sys
    if sys.platform != "darwin":
        return {}

    script = (
        'tell application "Google Chrome"\n'
        "    set tabTitle to title of active tab of front window\n"
        "    set tabURL to URL of active tab of front window\n"
        '    return tabTitle & "|" & tabURL\n'
        "end tell"
    )
    try:
        proc = await asyncio.create_subprocess_exec(
            "osascript", "-e", script,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await proc.communicate()
        if proc.returncode == 0:
            result = stdout.decode().strip()
            parts = result.split("|", 1)
            if len(parts) == 2:
                return {"title": parts[0], "url": parts[1]}
        return {}
    except Exception as e:
        log.warning(f"get_chrome_tab_info failed: {e}")
        return {}


async def monitor_build(project_dir: str, ws=None, synthesize_fn=None) -> None:
    """Monitor a Claude Code build for completion. Notify via WebSocket when done."""
    import base64

    output_file = Path(project_dir) / ".jarvis_output.txt"
    start = time.time()
    timeout = 600  # 10 minutes

    while time.time() - start < timeout:
        await asyncio.sleep(5)
        if output_file.exists():
            content = output_file.read_text()
            if "--- JARVIS TASK COMPLETE ---" in content:
                log.info(f"Build complete in {project_dir}")
                if ws and synthesize_fn:
                    try:
                        msg = "The build is complete, sir."
                        audio_bytes = await synthesize_fn(msg)
                        if audio_bytes:
                            encoded = base64.b64encode(audio_bytes).decode()
                            await ws.send_json({"type": "status", "state": "speaking"})
                            await ws.send_json({"type": "audio", "data": encoded, "text": msg})
                            await ws.send_json({"type": "status", "state": "idle"})
                    except Exception as e:
                        log.warning(f"Build notification failed: {e}")
                return

    log.warning(f"Build timed out in {project_dir}")


async def execute_action(intent: dict, projects: list = None) -> dict:
    """Route a classified intent to the right action function.

    Args:
        intent: {"action": str, "target": str} from classify_intent()
        projects: list of known project dicts for resolving working dirs

    Returns: {"success": bool, "confirmation": str, "project_dir": str | None}
    """
    action = intent.get("action", "chat")
    target = intent.get("target", "")

    if action == "open_terminal":
        claude_cmd = "claude --dangerously-skip-permissions" if _SKIP_PERMISSIONS else "claude"
        result = await open_terminal(claude_cmd)
        result["project_dir"] = None
        return result

    elif action == "browse":
        if target.startswith("http://") or target.startswith("https://"):
            url = target
        else:
            url = f"https://www.google.com/search?q={quote(target)}"

        # Detect which browser user wants
        target_lower = target.lower()
        if "firefox" in target_lower:
            browser = "firefox"
        else:
            browser = "chrome"

        result = await open_browser(url, browser)
        result["project_dir"] = None
        return result

    elif action == "build":
        # Create project folder on Desktop, spawn Claude Code
        project_name = _generate_project_name(target)
        project_dir = str(DESKTOP_PATH / project_name)
        os.makedirs(project_dir, exist_ok=True)
        result = await open_claude_in_project(project_dir, target)
        result["project_dir"] = project_dir
        return result

    elif action == "open_app":
        result = await open_app(target)
        result["project_dir"] = None
        return result

    elif action == "write_notepad":
        result = await write_notepad(target)
        result["project_dir"] = None
        return result

    else:
        return {"success": False, "confirmation": "", "project_dir": None}


def _generate_project_name(prompt: str) -> str:
    """Generate a kebab-case project folder name from the prompt."""
    # First: check for a quoted name like "tiktok-analytics-dashboard"
    quoted = re.search(r'"([^"]+)"', prompt)
    if quoted:
        name = quoted.group(1).strip()
        # Already kebab-case or close to it
        name = re.sub(r"[^a-zA-Z0-9\s-]", "", name).strip()
        if name:
            return re.sub(r"[\s]+", "-", name.lower())

    # Second: check for "called X" or "named X" pattern
    called = re.search(r'(?:called|named)\s+(\S+(?:[-_]\S+)*)', prompt, re.IGNORECASE)
    if called:
        name = re.sub(r"[^a-zA-Z0-9-]", "", called.group(1))
        if len(name) > 3:
            return name.lower()

    # Fallback: extract meaningful words
    words = re.sub(r"[^a-zA-Z0-9\s]", "", prompt.lower()).split()
    skip = {"a", "the", "an", "me", "build", "create", "make", "for", "with", "and",
            "to", "of", "i", "want", "need", "new", "project", "directory", "called",
            "on", "desktop", "that", "application", "app", "full", "stack", "simple",
            "web", "page", "site", "named"}
    meaningful = [w for w in words if w not in skip and len(w) > 2][:4]
    return "-".join(meaningful) if meaningful else "jarvis-project"


async def open_app(app_name: str) -> dict:
    """Open an installed application on the user's computer."""
    import sys
    import subprocess
    success = False
    
    app_clean = app_name.strip().lower()
    
    # Common Windows executable mappings
    windows_mappings = {
        "vs code": "code",
        "vscode": "code",
        "visual studio code": "code",
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "word": "winword",
        "excel": "excel",
        "powerpoint": "powerpnt",
        "browser": "chrome",
        "google chrome": "chrome",
        "firefox": "firefox",
        "edge": "msedge",
        "spotify": "spotify",
        "slack": "slack",
        "discord": "discord",
        "zoom": "zoom",
    }
    
    if sys.platform == "win32":
        cmd_target = windows_mappings.get(app_clean, app_clean)
        try:
            subprocess.Popen(f'start "" "{cmd_target}"', shell=True)
            success = True
        except Exception as e:
            log.error(f"Failed to open app {app_clean} (mapped: {cmd_target}) on Windows: {e}")
            
    elif sys.platform == "darwin":
        # macOS: use open -a
        try:
            subprocess.Popen(["open", "-a", app_clean])
            success = True
        except Exception as e:
            log.error(f"Failed to open app {app_clean} on macOS: {e}")
            
    else:
        try:
            subprocess.Popen([app_clean])
            success = True
        except Exception as e:
            log.error(f"Failed to open app {app_clean} on Linux: {e}")

    return {
        "success": success,
        "confirmation": f"Opening {app_name}, sir." if success else f"I had trouble opening {app_name}, sir."
    }


async def write_notepad(text: str) -> dict:
    """Write text to a temporary text file and open it in Notepad on Windows."""
    import sys
    import tempfile
    import subprocess
    from pathlib import Path
    
    success = False
    if sys.platform == "win32":
        try:
            desktop = Path.home() / "Desktop"
            if desktop.exists():
                file_path = desktop / "JARVIS_Note.txt"
            else:
                file_path = Path(tempfile.gettempdir()) / "JARVIS_Note.txt"
                
            file_path.write_text(text, encoding="utf-8")
            subprocess.Popen(f'start notepad.exe "{file_path}"', shell=True)
            success = True
            confirmation = f"I've written that in Notepad for you, sir. It is saved as JARVIS_Note.txt on your Desktop."
        except Exception as e:
            log.error(f"Failed to write in Notepad: {e}")
            confirmation = "I ran into an issue writing to Notepad, sir."
    else:
        # macOS / Linux fallback
        try:
            with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
                f.write(text.encode("utf-8"))
                tmp_path = f.name
            if sys.platform == "darwin":
                subprocess.Popen(["open", "-t", tmp_path])
            else:
                subprocess.Popen(["xdg-open", tmp_path])
            success = True
            confirmation = "I've opened the text in your editor, sir."
        except Exception:
            confirmation = "Action not supported on this platform, sir."
            
    return {"success": success, "confirmation": confirmation}
