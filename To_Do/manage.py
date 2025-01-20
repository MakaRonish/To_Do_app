#!/usr/bin/env python
import os
import sys

# Apply monkey-patch if we are running the huey consumer.
if "run_huey" in sys.argv:  # Check if the command is 'run_huey'
    from gevent import monkey  # Import the monkey-patching module

    monkey.patch_all()  # Apply the patch to make I/O non-blocking

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "To_Do.settings"
    )  # Replace 'your_project_name' with your Django project name
    from django.core.management import (
        execute_from_command_line,
    )  # Import Django's command-line executor

    execute_from_command_line(sys.argv)  # Execute the command
