import PySimpleGUI as sg
import requests
import json


class MessengerUI:

    def __init__(self):

        layout = [
            [sg.Text('URL', size=(6, 1)), sg.InputText(key="url")],
            [sg.Text('Method'), sg.Combo([
                "GET"
                # , "POST", "DELETE"
            ],
                size=(12, 1), key="method_type")],
            [sg.Text("Headers")],
            [sg.Multiline("Content-Type: application/json",
                          size=(45, 5), key="headers")],
            [sg.Button("DELIVER")]
        ]

        window = sg.Window("MessengerLite", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == "DELIVER":
                for i in range(1, 20):
                    sg.one_line_progress_meter(
                        'Request Progress', i+1, 20, 'Sending Request')
                self.RequestManager(event, values)
                break

        window.close()

    def RequestManager(self, event, values):

        if values["method_type"] == "GET":

            try:

                req = requests.get(
                    values["url"], headers=self.HeadersManager(values["headers"]))
                sg.popup(req.text)

            except:

                sg.popup("Request Failed | Perhaps an invalid URL, unstable connection or invalid headers.",
                         text_color="#ff0000", auto_close=False)

    def HeadersManager(self, headersStr):

        headersStr = headersStr.split("\n")
        json_data = "{"

        for headerLine in headersStr:

            header = headerLine.split(":")

            json_data += f"\"{header[0].strip()}\":\"{header[1].strip()}\","

        json_data = json_data[:-1]
        json_data += "}"

        return json.loads(json_data)


MessengerUI()
