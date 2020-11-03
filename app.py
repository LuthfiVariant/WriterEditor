class Article:
    def __init__(self, judul, penulis, editor, status):
        self.judul = judul
        self.penulis = penulis
        self.editor = editor
        self.editor2 = None
        self.status = status #harusnya ada 2 pilihan on-progress atau finished
        self.revision = None
    
    def get_team(self):
        if self.editor2 == None:
            return self.penulis, self.editor
        else:
            return  self.penulis, self.editor, self.editor2

    def change_writer(self, penulisBaru):
        self.penulis = penulisBaru
    
    def change_editor(self, editorBaru):
        self.editor = editorBaru

    def add_editor(self, editor2):
        self.editor2 = editor2

    def get_status(self):
        return self.status

    def publish(self, status):
        self.status = "Finished"

class Petugas:
    def __init__(self, nama, kontak, email, role):
        self.nama = nama
        self.kontak = kontak
        self.email = email
        self.role = role #harusnya ada 2: penulis atau editor
        self.project = []

    def get_role(self):
        return self.role

    def get_contact(self):
        return self.email, self.kontak

    def add_project(self, project):
        self.project.append((project, self.role))
        return self.project

    def get_project(self):
        return len(self.project)




