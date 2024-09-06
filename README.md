# PDF Interpreter - Preprocessing documents by reading charts and translating to English
## Running instructions
Navigate to the repository and then execute the following instructions:
```bash
docker build -t pdf-translator .
```bash
docker run -v <local path to files to translate>:/data -v <local path to save translated files>:/processed_data pdf-translator /data

Documents in these language might not need to get interpreted, as copilots understand them:
Chinese (Simplified) (zh-CN)
Czech (Czech Republic) (cs-CZ)
Danish (Denmark) (da-DK)
Dutch (Netherlands) (nl-NL)
English (Australia) (en-AU)
English (United Kingdom) (en-GB)
Finnish (Finland) (fi-FI)
French (France) (fr-FR)
French (Canada) (fr-CA)
German (Germany) (de-DE)
Greek (Greece) (el-GR)
Hindi (India) (hi-IN)
Indonesian (Indonesia) (id-ID)
Italian (Italy) (it-IT)
Japanese (Japan) (ja-JP)
Korean (Korea) (ko-KR)
Norwegian Bokmål (Norway) (nb-NO)
Polish (Poland) (pl-PL)
Portuguese (Brazil) (pt-BR)
Russian (Russia) (ru-RU)
Spanish (Spain) (es-ES)
Spanish (United States) (es-US)
Swedish (Sweden) (sv-SE)
Thai (Thailand) (th-TH)
Turkish (Turkey) (tr-TR)
