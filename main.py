#!/usr/bin/env python3
"""JARVIS AI Assistant — Entry Point.

Launches the JARVIS GUI application with proper initialization,
logging, and environment validation.
"""
from __future__ import annotations

import os
import sys

# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    """Initialize and launch JARVIS."""
    # 1. Validate environment
    from config.settings import validate_environment
    env_status = validate_environment()
    
    # 2. Initialize logging
    from core.logger import get_logger
    logger = get_logger('Main')
    logger.info('='*60)
    logger.info('JARVIS AI Assistant starting up...')
    logger.info('='*60)
    
    # Log API status
    for provider, available in env_status.items():
        status = '✓' if available else '✗'
        logger.info(f'  {status} {provider}')
    
    # 3. Launch GUI
    try:
        from gui.app import JarvisApp
        app = JarvisApp()
        app.mainloop()
    except Exception as e:
        logger.critical(f'Fatal error: {e}', exc_info=True)
        raise
    finally:
        logger.info('JARVIS shutting down.')


if __name__ == '__main__':
    main()
