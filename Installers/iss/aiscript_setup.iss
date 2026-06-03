; AiScript v0.2.1.post1 Standalone Installer for Windows
; Inno Setup 6 Script

#define MyAppName "AiScript v0.2.1.post1"
#define MyAppVersion "0.2.1.post1"
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
OutputBaseFilename=AiScript_Setup_v0.2.1.post1
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin
DisableDirPage=no
DisableProgramGroupPage=yes
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayName=AiScript v0.2.1.post1
ChangesAssociations=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Components]
Name: "core"; Description: "AiScript interpreter + REPL"; Types: full compact custom; Flags: fixed
Name: "ide"; Description: "Kite IDE (code editor + runner for .ais files)"; Types: full custom

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: checkedonce
Name: "associateais"; Description: "Associate .ais files with AiScript"; GroupDescription: "File associations:"; Flags: checkedonce

[Files]
Source: "..\..\AiScript\aiscript.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.0.1.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.0.2.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.1.4.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.1.3.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.2.0.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.2.0.post1.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.2.0.post2.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.2.1.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_v0.2.1.post1.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_ide_v0.2.1.post1.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\hbpe_compat.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\test_aiscript.ais"; DestDir: "{app}\examples"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\test_aiscript_v0.0.2.ais"; DestDir: "{app}\examples"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\test_aiscript_extra.ais"; DestDir: "{app}\examples"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_ide.py"; DestDir: "{app}"; Components: ide; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_ide_v0.1.3.py"; DestDir: "{app}\versions"; Components: core; Flags: ignoreversion
Source: "..\..\AiScript\kite.cmd"; DestDir: "{app}"; Components: ide; Flags: ignoreversion

[Icons]
Name: "{group}\AiScript 0.2.1.post1 REPL"; Filename: "{sys}\cmd.exe"; Parameters: "/C python ""{app}\aiscript.py"""; WorkingDir: {app}; Components: core; Comment: "AiScript interactive REPL"
Name: "{group}\Kite IDE (0.2.1.post1)"; Filename: "{app}\kite.cmd"; Parameters: ""; Components: ide; WorkingDir: {app}
Name: "{group}\Uninstall AiScript"; Filename: "{uninstallexe}"
Name: "{commondesktop}\AiScript 0.2.1.post1 REPL"; Filename: "{sys}\cmd.exe"; Parameters: "/C python ""{app}\aiscript.py"""; Tasks: desktopicon; WorkingDir: {app}

[Registry]
; Default association (double-click) — only with task
; HKLM64 avoids WOW6432Node redirection (32-bit installer → invisible to 64-bit Explorer)
Root: HKLM64; Subkey: "Software\Classes\.ais"; ValueType: string; ValueName: ""; ValueData: "AiScriptFile"; Tasks: associateais; Flags: uninsdeletevalue
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile"; ValueType: string; ValueName: ""; ValueData: "AiScript Source File"; Tasks: associateais; Flags: uninsdeletekey
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\kite.cmd"" ""%1"""; Tasks: associateais
; Right-click "Edit in Kite" — always if IDE component selected
; Register under BOTH extension and ProgID for maximum reliability
Root: HKLM64; Subkey: "Software\Classes\.ais\shell\Edit in Kite"; ValueType: string; ValueName: ""; ValueData: "Edit in Kite"; Components: ide; Flags: uninsdeletekey
Root: HKLM64; Subkey: "Software\Classes\.ais\shell\Edit in Kite\command"; ValueType: string; ValueName: ""; ValueData: """{app}\kite.cmd"" ""%1"""; Components: ide
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\Edit in Kite"; ValueType: string; ValueName: ""; ValueData: "Edit in Kite"; Components: ide; Flags: uninsdeletekey
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\Edit in Kite\command"; ValueType: string; ValueName: ""; ValueData: """{app}\kite.cmd"" ""%1"""; Components: ide
