"""
JARVIS Browser Control — voice-driven browser tab management.

Uses pyautogui (keyboard shortcuts) + pygetwindow (window focus).
Works with any browser: Chrome, Firefox, Edge.

Supported commands:
  scroll up / scroll down
  next tab / previous tab
  new tab / close tab
  go back / go forward
  refresh / reload
  zoom in / zoom out
  open incognito
"""

import asyncio
import logging
import sys
import time

log = logging.getLogger("jarvis.browser_control")

# Browser window title keywords to search for (in priority order)
_BROWSER_TITLES = ["Google Chrome", "Chrome", "Mozilla Firefox", "Firefox",
                   "Microsoft Edge", "Edge", "Brave", "Opera"]


def _focus_browser() -> bool:
    """Find an open browser window and bring it to focus.

    Returns True if a browser window was found and focused, False otherwise.
    Only works on Windows (pygetwindow is Windows-only).
    """
    if sys.platform != "win32":
        return False

    try:
        import pygetwindow as gw
        for title_keyword in _BROWSER_TITLES:
            windows = gw.getWindowsWithTitle(title_keyword)
            if windows:
                win = windows[0]
                try:
                    if win.isMinimized:
                        win.restore()
                    win.activate()
                    time.sleep(0.3)  # wait for window to come to front
                    return True
                except Exception:
                    continue
        return False
    except ImportError:
        log.warning("pygetwindow not installed. Run: pip install pygetwindow")
        return False
    except Exception as e:
        log.error(f"Window focus failed: {e}")
        return False


async def _send_shortcut(focus_first: bool = True, *keys) -> dict:
    """Focus browser then fire a keyboard shortcut."""
    if sys.platform != "win32":
        return {"success": False, "confirmation": "Browser control is only supported on Windows, sir."}

    try:
        import pyautogui
        pyautogui.FAILSAFE = False

        loop = asyncio.get_running_loop()

        def _do():
            if focus_first:
                found = _focus_browser()
                if not found:
                    return False
                time.sleep(0.15)
            if len(keys) == 1:
                pyautogui.press(keys[0])
            else:
                pyautogui.hotkey(*keys)
            return True

        result = await loop.run_in_executor(None, _do)
        return {"success": result, "confirmation": None}

    except ImportError:
        log.warning("pyautogui not installed. Run: pip install pyautogui")
        return {"success": False, "confirmation": "pyautogui is not installed, sir. Run: pip install pyautogui"}
    except Exception as e:
        log.error(f"Shortcut failed: {e}")
        return {"success": False, "confirmation": "Something went wrong with browser control, sir."}


# ---------------------------------------------------------------------------
# Public API — one function per action
# ---------------------------------------------------------------------------

async def scroll_down(amount: int = 3) -> str:
    for _ in range(amount):
        r = await _send_shortcut(True, "pagedown")
        if not r["success"]:
            return r["confirmation"] or "Browser not found, sir."
    return "Scrolling down, sir."


async def scroll_up(amount: int = 3) -> str:
    for _ in range(amount):
        r = await _send_shortcut(True, "pageup")
        if not r["success"]:
            return r["confirmation"] or "Browser not found, sir."
    return "Scrolling up, sir."


async def next_tab() -> str:
    r = await _send_shortcut(True, "ctrl", "tab")
    if not r["success"]:
        return r["confirmation"] or "Couldn't switch tab, sir."
    return "Next tab, sir."


async def prev_tab() -> str:
    r = await _send_shortcut(True, "ctrl", "shift", "tab")
    if not r["success"]:
        return r["confirmation"] or "Couldn't switch tab, sir."
    return "Previous tab, sir."


async def new_tab() -> str:
    r = await _send_shortcut(True, "ctrl", "t")
    if not r["success"]:
        return r["confirmation"] or "Couldn't open a new tab, sir."
    return "New tab opened, sir."


async def close_tab() -> str:
    r = await _send_shortcut(True, "ctrl", "w")
    if not r["success"]:
        return r["confirmation"] or "Couldn't close the tab, sir."
    return "Tab closed, sir."


async def go_back() -> str:
    r = await _send_shortcut(True, "alt", "left")
    if not r["success"]:
        return r["confirmation"] or "Couldn't go back, sir."
    return "Going back, sir."


async def go_forward() -> str:
    r = await _send_shortcut(True, "alt", "right")
    if not r["success"]:
        return r["confirmation"] or "Couldn't go forward, sir."
    return "Going forward, sir."


async def refresh_page() -> str:
    r = await _send_shortcut(True, "f5")
    if not r["success"]:
        return r["confirmation"] or "Couldn't refresh, sir."
    return "Page refreshed, sir."


async def zoom_in() -> str:
    r = await _send_shortcut(True, "ctrl", "+")
    if not r["success"]:
        return r["confirmation"] or "Couldn't zoom in, sir."
    return "Zoomed in, sir."


async def zoom_out() -> str:
    r = await _send_shortcut(True, "ctrl", "-")
    if not r["success"]:
        return r["confirmation"] or "Couldn't zoom out, sir."
    return "Zoomed out, sir."


async def zoom_reset() -> str:
    r = await _send_shortcut(True, "ctrl", "0")
    if not r["success"]:
        return r["confirmation"] or "Couldn't reset zoom, sir."
    return "Zoom reset to default, sir."


async def open_incognito() -> str:
    r = await _send_shortcut(True, "ctrl", "shift", "n")
    if not r["success"]:
        return r["confirmation"] or "Couldn't open incognito, sir."
    return "Incognito window opened, sir."


async def focus_address_bar() -> str:
    r = await _send_shortcut(True, "ctrl", "l")
    if not r["success"]:
        return r["confirmation"] or "Couldn't focus the address bar, sir."
    return "Address bar focused, sir."


# ---------------------------------------------------------------------------
# Dispatcher — maps a command string to an action
# ---------------------------------------------------------------------------

_COMMAND_MAP = {
    # scroll
    "scroll down":       scroll_down,
    "scroll up":         scroll_up,
    "page down":         scroll_down,
    "page up":           scroll_up,
    # tabs
    "next tab":          next_tab,
    "previous tab":      prev_tab,
    "prev tab":          prev_tab,
    "new tab":           new_tab,
    "close tab":         close_tab,
    "open new tab":      new_tab,
    # navigation
    "go back":           go_back,
    "go forward":        go_forward,
    "back":              go_back,
    "forward":           go_forward,
    # refresh
    "refresh":           refresh_page,
    "reload":            refresh_page,
    "refresh page":      refresh_page,
    "reload page":       refresh_page,
    # zoom
    "zoom in":           zoom_in,
    "zoom out":          zoom_out,
    "zoom reset":        zoom_reset,
    "reset zoom":        zoom_reset,
    # other
    "incognito":         open_incognito,
    "open incognito":    open_incognito,
    "private window":    open_incognito,
    "address bar":       focus_address_bar,
    "focus address bar": focus_address_bar,
    "search bar":        focus_address_bar,
}


async def execute(command: str) -> str:
    """Execute a browser control command by name."""
    cmd = command.strip().lower()
    fn = _COMMAND_MAP.get(cmd)
    if fn:
        return await fn()
    return f"I don't know the browser command '{command}', sir."
