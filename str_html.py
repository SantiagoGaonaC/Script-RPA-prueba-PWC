def html_estructura(df,i):
    html =(f"""<!DOCTYPE html>
<html lang="en">

<body>
    <p>Estimado encargado,<br>
    <p>Remito información sobre el pedido {df['Codigo_recepcion'][i]}<br>
    <table class="tg" style="border-collapse: collapse;
    border-spacing: 0;">
        <thead>
            <tr>
                <th class="tg-fymr" colspan="2" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                font-weight: normal;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top
                ">Envío:</th>
                <th class="tg-0pky" colspan="2" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                font-weight: normal;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Envio'][i]}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="tg-fymr" colspan="2" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Nombre:</td>
                <td class="tg-0pky" colspan="2" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Nombre'][i]}</td>
            </tr>
            <tr>
                <td class="tg-fymr" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Correo:</td>
                <td class="tg-0pky" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Correo'][i]}</td>
                <td class="tg-fymr" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Dominio:</td>
                <td class="tg-0pky" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Dominio'][i]}</td>
            </tr>
            <tr>
                <td class="tg-fymr" colspan="2" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Teléfono:</td>
                <td class="tg-0pky" colspan="2" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Teléfono'][i]}</td>
            </tr>
            <tr>
                <td class="tg-fymr" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Dirección:</td>
                <td class="tg-0pky" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Dirección'][i]}</td>
                <td class="tg-fymr" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Código Postal:</td>
                <td class="tg-0pky" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Codigo_Postal'][i]}</td>
            </tr>
            <tr>
                <td class="tg-fymr" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Repuestos:</td>
                <td class="tg-0pky" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Repuestos'][i]}</td>
                <td class="tg-fymr" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;
                border-color: inherit;
            font-weight: bold;
            text-align: left;
            vertical-align: top">Marca:</td>
                <td class="tg-0pky" style="border-color: black;
                border-style: solid;
                border-width: 1px;
                font-family: Arial, sans-serif;
                font-size: 14px;
                overflow: hidden;
                padding: 10px 5px;
                word-break: normal;">{df['Marca'][i]}</td>
            </tr>
        </tbody>
    </table>
    <br>
    <p>Saludos.
</body>
</html>
       """)
    return html