"""
Screenshot-Based AI Desktop Assistant
Entry point for launching the application.
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from capture.snip_tool import launch_tool

if __name__ == "__main__":
    print("🚀 Starting Eclip AI Desktop Assistant...")
    print("📸 Press Ctrl+Alt+X to capture a screenshot")
    print("⚙️  Right-click system tray icon for settings")
    launch_tool()
