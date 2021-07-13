import PySimpleGUI as sg


file_name = "/home/jostautas/Documents/gits/gimtadieniai/duom_failai/PVZ.txt"
f = open(file_name)

Months = ["1. Jan", "2. Feb", "3. Mar", "4. Apr", "5. May", "6. Jun", "7. Jul", "8. Aug", "9. Sep", "10. Oct", "11. Nov", "12. Dec"]

layout = [
        [sg.Text(" " * 97), sg.Text("Month:", justification='center', font=("Any 14"))],
        [sg.Button(Months[0], size=(15, 5)), sg.Button(Months[1], size=(15, 5)), sg.Button(Months[2], size=(15, 5)), sg.Button(Months[3], size=(15, 5)),
            sg.Button(Months[4], size=(15, 5)), sg.Button(Months[5], size=(15, 5))],
        [sg.Button(Months[6], size=(15, 5)), sg.Button(Months[7], size=(15, 5)), sg.Button(Months[8], size=(15, 5)), sg.Button(Months[9], size=(15, 5)),
            sg.Button(Months[10], size=(15, 5)), sg.Button(Months[11], size=(15, 5))],
        [sg.Text("Enter or delete the name of the event and its day of month:", font=("Any 12"))],
        [sg.Multiline("EXAMPLE:" + '\n' + f.read(), key="override", size=(80, 10))]
    ]

window = sg.Window("annual reminder", layout, size=(880, 400))

if __name__ == '__main__':
    while True:  # main event loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event:
            for x in Months:
                if event == x:
                    file_name = "/home/jostautas/Documents/gits/gimtadieniai/duom_failai/" + x + ".txt"
                    f = open(file_name)
                    window["override"].Update(f.read())  # prints out contents of a selected file in the sg.Multiline() (line 21)
                    # print(values[0])
    window.close()
