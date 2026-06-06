; AiScript v0.1.1 Installer (historical archive)
; Inno Setup 6 Script
#define MyAppName "AiScript v0.1.1"
#define MyAppVersion "0.1.1"
#define MyAppPublisher "AI.py Project"
#define MyAppURL "https://github.com/Voice659/AI-repo"
[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=output
OutputBaseFilename=AiScript_Setup_v0.1.1
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin
DisableDirPage=no
DisableProgramGroupPage=yes
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayName=AiScript v0.1.1
ChangesAssociations=yes
[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: checkedonce
Name: "associateais"; Description: "Associate .ais files with AiScript"; GroupDescription: "File associations:"; Flags: checkedonce
[Files]
Source: "..\..\..\AiScript\backups\aiscript_v0.0.2.py"; DestDir: "{app}"; DestName: "aiscript.py"; Flags: ignoreversion
Source: "..\..\..\AiScript\backups\aiscript_ide_v0.1.1.py"; DestDir: "{app}"; DestName: "aiscript_ide.py"; Flags: ignoreversion
Source: "..\..\..\AiScript\test_aiscript.ais"; DestDir: "{app}\examples"; Flags: ignoreversion
Source: "..\..\..\AiScript\test_aiscript_v0.0.2.ais"; DestDir: "{app}\examples"; Flags: ignoreversion
[Icons]
Name: "{group}\AiScript 0.1.1 REPL"; Filename: "{sys}\cmd.exe"; Parameters: "/K python ""{app}\aiscript.py"""; WorkingDir: {app}
Name: "{group}\Kite IDE (0.1.1)"; Filename: "{sys}\cmd.exe"; Parameters: "/K pythonw ""{app}\aiscript_ide.py"""; WorkingDir: {app}
Name: "{group}\Uninstall AiScript"; Filename: "{uninstallexe}"
Name: "{commondesktop}\AiScript 0.1.1 REPL"; Filename: "{sys}\cmd.exe"; Parameters: "/K python ""{app}\aiscript.py"""; WorkingDir: {app}
[Registry]
Root: HKLM64; Subkey: "Software\Classes\.ais"; ValueType: string; ValueName: ""; ValueData: "AiScriptFile"; Tasks: associateais; Flags: uninsdeletevalue
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile"; ValueType: string; ValueName: ""; ValueData: "AiScript Source File"; Tasks: associateais; Flags: uninsdeletekey
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{sys}\python.exe"" ""{app}\aiscript.py"" ""%1"""; Tasks: associateais
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\Edit in Kite\command"; ValueType: string; ValueName: ""; ValueData: """{sys}\pythonw.exe"" ""{app}\aiscript_ide.py"" ""%1"""; Flags: uninsdeletekey
