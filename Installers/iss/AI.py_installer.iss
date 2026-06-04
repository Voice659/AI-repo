; AI.py v6.0.0 Installer with AiScript components
; Inno Setup 6 Script

#define MyAppName "AI.py v6.0.0"
#define MyAppVersion "6.0.0"
#define MyAIScriptVersion "0.3.0.post2"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=output
OutputBaseFilename=AI.py_Setup_v6.0.0
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin
DisableDirPage=no
DisableProgramGroupPage=yes
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayName=AI.py v6.0.0
ChangesAssociations=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Components]
Name: "core"; Description: "AI.py v6.0.0 (core interpreter)"; Types: full compact custom; Flags: fixed
Name: "aiscript"; Description: "AiScript {#MyAIScriptVersion} interpreter + REPL + Kite IDE"; Types: full compact custom; Flags: fixed
Name: "hbpe_stable"; Description: "HubBasePE (stable, pip install hbpe)"; Types: full custom
Name: "hbpe_dev"; Description: "HubBasePE (development version, pip install hbpe==dev)"; Types: custom
Name: "data_bulk_1_3"; Description: "Data Bulk files 1-3"; Types: full custom
Name: "data_bulk_4_10"; Description: "Data Bulk files 4-10"; Types: full custom
Name: "data_bulk_11_20"; Description: "Data Bulk files 11-20"; Types: full custom
Name: "data_bulk_21_31"; Description: "Data Bulk files 21-31"; Types: full custom
Name: "data_files"; Description: "Data files (post-install note)"; Types: custom; Flags: checkablealone

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: checkedonce
Name: "associateais"; Description: "Associate .ais files with AiScript"; GroupDescription: "File associations:"; Flags: checkedonce

[Files]
; Core AI.py
Source: "..\..\AI.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\AIpy\installer.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion

; AiScript core files (versioned subdirectory)
Source: "..\..\AiScript\aiscript.py"; DestDir: "{app}\AiScript {#MyAIScriptVersion}"; Components: aiscript; Flags: ignoreversion
Source: "..\..\AiScript\aiscript.py"; DestDir: "{app}"; Components: aiscript; Flags: ignoreversion
Source: "..\..\AiScript\aiscript_ide.py"; DestDir: "{app}\AiScript {#MyAIScriptVersion}"; Components: aiscript; Flags: ignoreversion
Source: "..\..\AiScript\kite.cmd"; DestDir: "{app}\AiScript {#MyAIScriptVersion}"; Components: aiscript; Flags: ignoreversion
Source: "..\..\AiScript\test_aiscript.ais"; DestDir: "{app}\AiScript {#MyAIScriptVersion}\examples"; Components: aiscript; Flags: ignoreversion
Source: "..\..\AiScript\test_aiscript_v0.0.2.ais"; DestDir: "{app}\AiScript {#MyAIScriptVersion}\examples"; Components: aiscript; Flags: ignoreversion
Source: "..\..\AiScript\test_aiscript_extra.ais"; DestDir: "{app}\AiScript {#MyAIScriptVersion}\examples"; Components: aiscript; Flags: ignoreversion
Source: "..\..\hbpe_compat.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\..\Json\*"; DestDir: "{app}\Json"; Components: core; Flags: ignoreversion recursesubdirs
Source: "..\..\HBPE\**"; DestDir: "{app}\HBPE"; Components: core; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\AI.py v6.0.0"; Filename: "{sys}\cmd.exe"; Parameters: "/C python ""{app}\AI.py"""; WorkingDir: {app}; Components: core; Comment: "AI.py v6.0.0 CLI"
Name: "{group}\AiScript {#MyAIScriptVersion} REPL"; Filename: "{sys}\cmd.exe"; Parameters: "/C python ""{app}\AiScript {#MyAIScriptVersion}\aiscript.py"""; WorkingDir: {app}\AiScript {#MyAIScriptVersion}; Components: aiscript; Comment: "AiScript interactive REPL"
Name: "{group}\Kite IDE ({#MyAIScriptVersion})"; Filename: "{app}\AiScript {#MyAIScriptVersion}\kite.cmd"; Parameters: ""; Components: aiscript; WorkingDir: {app}\AiScript {#MyAIScriptVersion}
Name: "{group}\Uninstall AI.py"; Filename: "{uninstallexe}"
Name: "{commondesktop}\AI.py v6.0.0"; Filename: "{sys}\cmd.exe"; Parameters: "/C python ""{app}\AI.py"""; WorkingDir: {app}

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  ResultCode: Integer;
begin
  if CurStep = ssInstall then
  begin
    Exec('reg.exe', 'delete "HKLM\Software\Classes\.ais\shell\Edit in Kite" /reg:64 /f', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    Exec('reg.exe', 'delete "HKLM\Software\Classes\AiScriptFile\shell\Edit in Kite" /reg:64 /f', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  end;
end;

[Registry]
; File association for .ais
Root: HKLM64; Subkey: "Software\Classes\.ais"; ValueType: string; ValueName: ""; ValueData: "AiScriptFile"; Tasks: associateais; Flags: uninsdeletevalue
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile"; ValueType: string; ValueName: ""; ValueData: "AiScript Source File"; Tasks: associateais; Flags: uninsdeletekey
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\AiScript {#MyAIScriptVersion}\kite.cmd"" ""%1"""; Tasks: associateais

; Right-click "Edit in Kite" — cascading menu with versioned sub-items
; Old flat command key deleted via [Code] at ssInstall, before [Registry] runs
; Parent cascade (no uninsdeletekey — other versions may also use it)
Root: HKLM64; Subkey: "Software\Classes\.ais\shell\Edit in Kite"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Edit in Kite"; Components: aiscript
Root: HKLM64; Subkey: "Software\Classes\.ais\shell\Edit in Kite"; ValueType: string; ValueName: "subcommands"; ValueData: ""; Components: aiscript
; Version-specific sub-item (uninsdeletekey — clean on uninstall)
; 02- prefix sorts after standalone installer's 01-
Root: HKLM64; Subkey: "Software\Classes\.ais\shell\Edit in Kite\shell\02-Kite v0.3.0.post2 (AI.py)"; ValueType: string; ValueName: ""; ValueData: "Kite v0.3.0.post2 (AI.py)"; Components: aiscript; Flags: uninsdeletekey
Root: HKLM64; Subkey: "Software\Classes\.ais\shell\Edit in Kite\shell\02-Kite v0.3.0.post2 (AI.py)\command"; ValueType: string; ValueName: ""; ValueData: """{app}\AiScript {#MyAIScriptVersion}\kite.cmd"" ""%1"""; Components: aiscript
; Same for AiScriptFile ProgID
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\Edit in Kite"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Edit in Kite"; Components: aiscript
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\Edit in Kite"; ValueType: string; ValueName: "subcommands"; ValueData: ""; Components: aiscript
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\Edit in Kite\shell\02-Kite v0.3.0.post2 (AI.py)"; ValueType: string; ValueName: ""; ValueData: "Kite v0.3.0.post2 (AI.py)"; Components: aiscript; Flags: uninsdeletekey
Root: HKLM64; Subkey: "Software\Classes\AiScriptFile\shell\Edit in Kite\shell\02-Kite v0.3.0.post2 (AI.py)\command"; ValueType: string; ValueName: ""; ValueData: """{app}\AiScript {#MyAIScriptVersion}\kite.cmd"" ""%1"""; Components: aiscript

[Run]
; HBPE is now vendored via HBPE\** in [Files] — no pip install needed
; Components hbpe_stable/hbpe_dev remain for future use
