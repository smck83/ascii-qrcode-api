from fastapi import FastAPI

import convert
from fastapi.responses import HTMLResponse

app = FastAPI()



@app.get("/genAsciiQr")
def generate(text):
    htmlHeader = convert.import_txt_to_list('./output.html')
    asciiQrCode = convert.generateasciiQR(text, invert=False, white='██', black='  ', version=1, border=1, correction='M')
    htmlFooter = "</pre></div></body></html>"
    htmlOutput = "\n".join(htmlHeader) + asciiQrCode + htmlFooter
    return HTMLResponse(content=(htmlOutput), status_code=200)




