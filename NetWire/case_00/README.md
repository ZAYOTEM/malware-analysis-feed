# NetWire-Analysis-Scripts


- ```LogDecode.py``` scripti ile MD5 <em>"5c9ad0440fefa31403bd944a1a10a3b8"</em> hash değerine sahip NetWire zararlısının kaydettiği log dosyası içerisindeki tuş vuruşları ve mevcut uygulamaya ait *encrypt* edilmiş bilgiler çözülmektedir.



- ```StringDecode.py``` scripti ile MD5 <em>"5c9ad0440fefa31403bd944a1a10a3b8"</em>  hash değerine sahip NetWire zararlısının kaynaklarında bulundurduğu *obfuscate* edilmiş DLL, SQL sorguları, hedef tarayıcı bilgileri vb. hassas veriler deobfuscate edilmektedir.


## Kullanım

- ```.\LogDecode.py .\Logs```
- ```.\StringDecode.py .\strings.txt```


## Decrypt Edilen Log Örneği

```

[Log Started] - [25/10/2022 02:30:13]


[kprkpr.exe - PID: 78 - Modl: kprkpr.exe - Thread: Ana lem 8A8 - x32dbg] - [25/10/2022 02:30:13]
[F8]

[kprkpr.exe - PID: 78 - Modl: kprkpr.exe - Thread: Ana lem 8A8 - x32dbg] - [25/10/2022 02:30:13]
[F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][Backspace][Ctrl+][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8]

[Capturing from Yerel A Balants] - [25/10/2022 02:32:23]
S

[kprkpr.exe - PID: 78 - Modl: kprkpr.exe - Thread: Ana lem 8A8 - x32dbg] - [25/10/2022 02:34:24]
[F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8]a[Backspace]0[F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][Arrow Down][F2][Arrow Down][F2][Arrow Down][F2][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F9][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F9][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F9][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8]g[Ctrl+][Enter][Ctrl+][Ctrl+ ][Ctrl+][Enter][Arrow Up][Arrow Up][Arrow Up][Arrow Up][Arrow Down][Arrow Down][Arrow Down][Arrow Down][F9][F2][Arrow Down][F2][Arrow Down][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F2][F9][F9][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F2][F9][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F9]

[Log Started] - [25/10/2022 03:06:55]


[kprkpr.exe - PID: 73C - Modl: kprkpr.exe - Thread: Ana lem EBC - x32dbg] - [25/10/2022 03:06:55]
[F9]

[kprkpr.exe - PID: 73C - Modl: kprkpr.exe - Thread: Ana lem EBC - x32dbg] - [25/10/2022 03:09:16]
[F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8]

[Log Started] - [25/10/2022 03:10:44]


[kprkpr.exe - PID: C50 - Modl: kprkpr.exe - Thread: Ana lem C3C - x32dbg] - [25/10/2022 03:10:44]
[F8]

[kprkpr.exe - PID: C50 - Modl: kprkpr.exe - Thread: Ana lem C3C - x32dbg] - [25/10/2022 03:10:44]
[F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8]eax = FFFFFFF   ecx = 7EFDD000  edx = 273[Backspace]4C    ESP = 387D98[Ctrl+][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][Ctrl+][Ctrl+][F8][F8][F8][F8][F8][F9][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][Arrow Up][F2][Arrow Down][F9][F2][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][Arrow Up][Arrow Down][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F9][F9][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F9][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F9][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8]0x[Ctrl+][Enter]g[Ctrl+][Enter][Ctrl+]DE[F8][F8][F2][F9]

[Balat mens] - [25/10/2022 03:29:48]
DE

[Yeni Sekme - Google Chrome] - [25/10/2022 03:30:56]
uncapk.me[Enter]

[Log Started] - [25/10/2022 03:37:32]


[kprkpr.exe - PID: D70 - Modl: kprkpr.exe - Thread: Ana lem 920 - x32dbg] - [25/10/2022 03:37:32]
[F8]

[kprkpr.exe - PID: D70 - Modl: kprkpr.exe - Thread: Ana lem 920 - x32dbg] - [25/10/2022 03:37:32]
[F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F2][F2][F2][F7][F7]

[Log Started] - [25/10/2022 19:01:34]


[kprkpr.exe - PID: 9C0 - Modl: user32.dll - Thread: 758 - x32dbg] - [25/10/2022 18:10:15]
[F8]

[kprkpr.exe - PID: 9C0 - Modl: kprkpr.exe - Thread: 758 - x32dbg] - [25/10/2022 19:11:58]
[F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F7][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F7][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8][F8]

[Log Started] - [25/10/2022 19:45:09]


[kprkpr.exe - PID: 7C0 - Modl: kprkpr.exe - Thread: 6B4 - x32dbg] - [25/10/2022 19:44:55]
[F8]

[kprkpr.exe - PID: 7C0 - Modl: kprkpr.exe - Thread: 6B4 - x32dbg] - [25/10/2022 19:45:32]
[F8][F8][F8][F8][F8][F8][F8][F8][F9][F9][F9] 

```

## Deobfuscate Edilen Stringler

```
plds4.dll === siS6O.Sii 
plc4.dll === siYO.Sii 
nspr4.dll === R6s0O.Sii 
sqlite3.dll === 67i45dN.Sii
mozcrt19.dll === lWkY05Gt.Sii 
Secur32.dll === MdYQ0Nh.Sii 
nssutil3.dll === R66Q54iN.Sii
nss3.dll === R66N.Sii 
softokn3.dll === 6W85WwRN.Sii 
nssdbm3.dll === R66SVlN.Sii 
msvcr100.dll === l62Y0Gyy.Sii
msvcp100.dll === l62YsGyy.Sii 
msvcr120.dll === l62Y0Ghy.Sii 
msvcp120.dll === l62YsGhy.Sii 
api-ms-win-core-timezone-l1-1-0.dll === Cs43l63g4R3YW0d354ldkWRd3iG3G3y.Sii
api-ms-win-core-file-l2-1-0.dll === Cs43l63g4R3YW0d384id3ih3G3y.Sii
api-ms-win-core-file-l2-1-0.dll === Cs43l63g4R3YW0d384id3ih3G3y.Sii
api-ms-win-core-localization-l1-2-0.dll === Cs43l63g4R3YW0d3iWYCi4kC54WR3iG3h3y.Sii 
api-ms-win-core-synch-l1-2-0.dll === Cs43l63g4R3YW0d36ZRYI3iG3h3y.Sii
api-ms-win-core-processthreads-l1-1-1.dll === Cs43l63g4R3YW0d3s0WYd665I0dCS63iG3G3G.Sii 
api-ms-win-core-file-l1-2-0.dll === Cs43l63g4R3YW0d384id3iG3h3y.Sii 
api-ms-win-crt-runtime-l1-1-0.dll === Cs43l63g4R3Y0530QR54ld3iG3G3y.Sii 
api-ms-win-crt-string-l1-1-0.dll === Cs43l63g4R3Y0536504Rn3iG3G3y.Sii 
api-ms-win-crt-heap-l1-1-0.dll === Cs43l63g4R3Y053IdCs3iG3G3y.Sii 
api-ms-win-crt-stdio-l1-1-0.dll === Cs43l63g4R3Y05365S4W3iG3G3y.Sii 
api-ms-win-crt-convert-l1-1-0.dll === Cs43l63g4R3Y053YWR2d053iG3G3y.Sii 
api-ms-win-crt-locale-l1-1-0.dll === Cs43l63g4R3Y053iWYCid3iG3G3y.Sii
api-ms-win-crt-math-l1-1-0.dll === Cs43l63g4R3Y053lC5I3iG3G3y.Sii
api-ms-win-crt-multibyte-l1-1-0.dll === Cs43l63g4R3Y053lQi54VZ5d3iG3G3y.Sii 
api-ms-win-crt-time-l1-1-0.dll === Cs43l63g4R3Y05354ld3iG3G3y.Sii 
api-ms-win-crt-filesystem-l1-1-0.dll === Cs43l63g4R3Y05384id6Z65dl3iG3G3y.Sii 
api-ms-win-crt-environment-l1-1-0.dll === Cs43l63g4R3Y053dR240WRldR53iG3G3y.Sii
api-ms-win-crt-utility-l1-1-0.dll === Cs43l63g4R3Y053Q54i45Z3iG3G3y.Sii 
api-ms-win-core-string-l1-1-0.dll === Cs43l63g4R3YW0d36504Rn3iG3G3y.Sii 
api-ms-win-core-namedpipe-l1-1-0.dll === Cs43l63g4R3YW0d3RCldSs4sd3iG3G3y.Sii 
api-ms-win-core-handle-l1-1-0.dll === Cs43l63g4R3YW0d3ICRSid3iG3G3y.Sii 
api-ms-win-core-heap-l1-1-0.dll === Cs43l63g4R3YW0d3IdCs3iG3G3y.Sii
api-ms-win-core-libraryloader-l1-1-0.dll === Cs43l63g4R3YW0d3i4V0C0ZiWCSd03iG3G3y.Sii
api-ms-win-core-synch-l1-1-0.dll === Cs43l63g4R3YW0d36ZRYI3iG3G3y.Sii 
api-ms-win-core-processthreads-l1-1-0.dll === Cs43l63g4R3YW0d3s0WYd665I0dCS63iG3G3y.Sii 
api-ms-win-core-processenvironment-l1-1-0.dll === Cs43l63g4R3YW0d3s0WYd66dR240WRldR53iG3G3y.Sii 
api-ms-win-core-datetime-l1-1-0.dll === Cs43l63g4R3YW0d3SC5d54ld3iG3G3y.Sii 
api-ms-win-core-sysinfo-l1-1-0.dll === Cs43l63g4R3YW0d36Z64R8W3iG3G3y.Sii 
api-ms-win-core-console-l1-1-0.dll === Cs43l63g4R3YW0d3YWR6Wid3iG3G3y.Sii 
api-ms-win-core-debug-l1-1-0.dll === Cs43l63g4R3YW0d3SdVQn3iG3G3y.Sii 
api-ms-win-core-profile-l1-1-0.dll === Cs43l63g4R3YW0d3s0W84id3iG3G3y.Sii 
api-ms-win-core-memory-l1-1-0.dll === Cs43l63g4R3YW0d3ldlW0Z3iG3G3y.Sii 
api-ms-win-core-util-l1-1-0.dll === Cs43l63g4R3YW0d3Q54i3iG3G3y.Sii 
api-ms-win-core-rtlsupport-l1-1-0.dll === Cs43l63g4R3YW0d305i6QssW053iG3G3y.Sii 
api-ms-win-core-interlocked-l1-1-0.dll === Cs43l63g4R3YW0d34R5d0iWYwdS3iG3G3y.Sii
ucrtbase.dll === QY05VC6d.Sii 
vcruntime140.dll === 2Y0QR54ldGOy.Sii 
msvcp140.dll === l62YsGOy.Sii
mozutils.dll === lWkQ54i6.Sii 
mozglue.dll === lWkniQd.Sii 
mozsqlite3.dll === lWk67i45dN.Sii
MozillaSeaMonkeyprofiles.ini === FWk4iiC\MdCFWRwdZ\s0W84id6.4R4 
signons.sqlite === 64nRWR6.67i45d 
logins.json === iWn4R6.e6WR 
purpleaccounts.xml === sQ0sid\CYYWQR56.fli 
Thunderbirdprofiles.ini === qIQRSd0V40S\s0W84id6.4R4 
sqlite3.close === 67i45dNpYiW6d
sqlite3.open === 67i45dNpWsdR 
sqlite3.prepare.v2 === 67i45dNps0dsC0dp2h 
sqlite3.step === 67i45dNp65ds 
sqlite3.column.text === 67i45dNpYWiQlRp5df5 
selectfrommoz.logins === 6didY5 *  80Wl lWkpiWn4R6
hostname === IW65RCld 
SMTppassword === MFq9 9C66gW0S 
EASUser === jDM u6d0 
EASServerUR === jDM Md02d0 urm
EASpassword === jDM 9C66gW0S 
crypt32.dll === Y0Zs5Nh.Sii 
CryptUnprotectData === P0Zs5uRs0W5dY5aC5C 
index.dat === 4RSdf.SC5 
vaultcli.dll === 2CQi5Yi4.Sii 
VaultOpenVault === zCQi5TsdRzCQi5
VaultCloseVault === zCQi5PiW6dzCQi5 
VaultEnumerateitems === zCQi5jRQld0C5dX5dl6 
VaultGetitem === zCQi5Ed5X5dl
system32cmd.exe === 6Z65dlNh\YlS.dfd 
GetNativeSysteminf === Ed5LC542dMZ65dlXR8 
kernel32.dll === wd0RdiNh.Sii
GlobalMemoryStatusEx === EiWVCiFdlW0ZM5C5Q6jf 
HARDWAREESCRipTiONSystemCentralprocessor0 === -DraUDrj jMPrX9qXTL\MZ65dl\PdR50Ci90WYd66W0\y
AllocateAndinitializeSid === DiiWYC5dDRSXR454Ci4kdM4S 
CheckTokenMembership === PIdYwqWwdRFdlVd06I4s
ESCRipTiON === jMPrX9qXTL 
```

