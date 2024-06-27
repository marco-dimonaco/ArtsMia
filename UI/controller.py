import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._view.txt_result.controls.clear()
        grafo = self._model.buildGraph()
        if grafo:
            self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato!", color='green'))
            self._view.txt_result.controls.append(ft.Text(self._model.printGraphDetails()))
            self._view._txtIdOggetto.disabled = False
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Errore nella creazione del grafo!", color='red'))
            self._view.update_page()
            return

    def checkId(self, e):
        idIn = self._view._txtIdOggetto.value
        try:
            intIdIn = int(idIn)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un id Oggetto intero!", color='red'))
            self._view.update_page()
            return
        check = self._model.checkId(int(idIn))
        if check:
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {idIn} è presente nel grafo"))
            self._view._btnCompConnessa.disabled = False
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {idIn} non è presente nel grafo"))
            self._view.update_page()
            return

    def handleCompConnessa(self, e):
        idIn = self._view._txtIdOggetto.value
        lConnComp = self._model.compConn(int(idIn))
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene {idIn} ha dimensione {lConnComp}"))
        self._view.update_page()
        return
