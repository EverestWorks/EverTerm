# Mod Framework Documentation

The mod framework is an extension to the terminal application that allows users to add custom commands without modifying the main application's source code. Users can create separate Python files, referred to as "mods," that define their custom commands. The main application dynamically loads these mods at runtime, making the custom commands available for use during the terminal session.

## Getting Started

To get started with the mod framework, follow these steps:

1. Create a new Python file for your mod. The file should have a `.py` extension.

2. Define your custom commands in the mod file as functions. Each command should take a single argument, `args`, which will be a string containing any arguments passed to the command.

   **Example of a mod file named `my_mod.py`:**

   ```python
   def custom_command(args):
       """Example custom command."""
       print("This is a custom command from my_mod.py.")
       print("Arguments provided:", args)

   # Add more custom commands here...
Place your mod file in the mods directory at the same level as the main_app.py script. If the mods directory does not exist, the application will create it automatically.

Run the main_app.py script. The main application will automatically load all the mods present in the mods directory.

## Using Custom Commands
Once the mods are loaded, you can use the custom commands in the terminal application. Simply enter the command name, followed by any arguments, and press Enter.

Example of using the custom command from my_mod.py:
----------------------------------
$: custom_command Hello, World!
This is a custom command from my_mod.py.
Arguments provided: Hello, World!

----------------------------------

## Error Handling
If there is an issue with a mod file (e.g., syntax errors, missing function definition), the application will display an error message indicating that the mod failed to load. Check the syntax and content of the mod file to resolve the issue.

## Mod Management
The mod framework provides a built-in mod management system. This system allows users to manage their mods using the following commands:

mod list: List all currently loaded mods.

mod load <mod_name>: Load a specific mod from the mods directory.

mod unload <mod_name>: Unload a specific mod, making its custom commands unavailable.

Examples of using the mod management commands:
------------------------------
$: mod list
Loaded Mods:
- my_mod



$: mod load new_mod
new_mod loaded successfully.

$: mod unload my_mod
my_mod unloaded successfully.
------------------------------
## Mod Naming Convention
To ensure that mods are recognized and loaded correctly, please follow these naming conventions:

Mod files should have a .py extension.
Mod file names should only contain letters, digits, and underscores (no spaces or special characters).
Avoid using Python keywords or built-in module names as mod file names.
## Tips
You can create multiple mod files, each defining different custom commands.
Mods can be added or modified while the application is running. The application will automatically pick up any changes in the mods directory.

## Summary
The mod framework allows users to extend the terminal application's functionality by defining custom commands in separate mod files. The application dynamically loads all the mods present in the mods directory, making the custom commands accessible during the terminal session. This provides users with the flexibility to tailor the application to their specific needs without having to modify the main application's source code.