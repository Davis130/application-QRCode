import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
 
class Main(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = QtWidgets.QWidget(self)
        self.setWindowTitle("Application QRCode")
        self.setCentralWidget(self.ui)
        self.setFixedSize(1000,400)

        self.ui.label_ville = QtWidgets.QLabel("Ville")
        self.ui.label_Site = QtWidgets.QLabel("Site")
        self.ui.label_stock = QtWidgets.QLabel("Stock")
        self.ui.label_entrepot_logique = QtWidgets.QLabel("Entrepôt Logique")
        self.ui.label_Etat_de_actif = QtWidgets.QLabel("Etat de l'actif")
        self.ui.label_sous_etat_actif = QtWidgets.QLabel("Sous-état de l'actif")
        self.ui.label_motif= QtWidgets.QLabel("Motif")
        self.ui.label_grade = QtWidgets.QLabel("Grade")
        self.ui.label_blanchiment = QtWidgets.QLabel("Blanchiment")
        self.ui.label_compte_gl = QtWidgets.QLabel("Compte GL")
        self.ui.label_id_rebut = QtWidgets.QLabel("ID Rebut")
        self.ui.label_ligne_qrcode = QtWidgets.QLabel("Ligne pour QRCode")

        
        
        self.ui.combo_ville = QtWidgets.QComboBox()
        self.ui.combo_site = QtWidgets.QComboBox()
        self.ui.combo_entrepot_physique = QtWidgets.QComboBox()
        self.ui.input_entrepot_logique = QtWidgets.QLineEdit()
        self.ui.combo_etat = QtWidgets.QComboBox()
        self.ui.combo_sous_etat = QtWidgets.QComboBox()
        self.ui.combo_motif = QtWidgets.QComboBox()
        self.ui.combo_grade = QtWidgets.QComboBox()
        self.ui.combo_blanchiment = QtWidgets.QComboBox()
        self.ui.input_compte_gl = QtWidgets.QLineEdit()
        self.ui.input_id_rebut = QtWidgets.QLineEdit()
        self.ui.input_ligne_qrcode = QtWidgets.QLineEdit()
        
        

        self.ui.combo_ville.addItems(("","Marseille",
                                        "Montpellier",
                                        "Nice",
                                        "Cruas",
                                        "Saint-Paul-Trois-Châteaux",
                                        "Lyon",
                                        "Saint-Alban",
                                        "Bugey",
                                        "Grenoble",
                                        "Chambéry"
                                        ))
        
        self.ui.combo_grade.addItems(("",
                                      "Grade A",
                                    "Grade B",
                                    "Grade C",
                                    "Grade D"
                                    ))
        
        self.ui.combo_blanchiment.addItems(("",
                                            "Blanchiment OK",
                                            "Blanchiment KO"
                                            ))
        
        self.ui.combo_ville.currentTextChanged.connect(self._updateCombo_site)
        self.ui.combo_site.currentTextChanged.connect(self._updateCombo_entrepot_physique)
        self.ui.combo_etat.currentTextChanged.connect(self._updateCombo_sous_etat)
        self.ui.combo_sous_etat.currentTextChanged.connect(self._updateCombo_motif)
        self.ui.combo_ville.currentTextChanged.connect(self._updateLineText)
        #self.ui.input_ligne_qrcode.insert(self.test)


        
        self.ui.combo_etat.addItems(("En stock","En cours d'utilisation","En cours de transit"))
        
 
        self.ui.layout = QtWidgets.QGridLayout()

        self.ui.layout.addWidget(self.ui.label_ville,1,0)
        self.ui.layout.addWidget(self.ui.label_Site,2,0)
        self.ui.layout.addWidget(self.ui.label_stock,3,0)
        self.ui.layout.addWidget(self.ui.label_entrepot_logique,4,0)
        self.ui.layout.addWidget(self.ui.label_Etat_de_actif,5,0)
        self.ui.layout.addWidget(self.ui.label_sous_etat_actif,6,0)
        self.ui.layout.addWidget(self.ui.label_motif,7,0)
        self.ui.layout.addWidget(self.ui.label_grade,8,0)
        self.ui.layout.addWidget(self.ui.label_blanchiment,9,0)
        self.ui.layout.addWidget(self.ui.label_compte_gl,10,0)
        self.ui.layout.addWidget(self.ui.label_id_rebut,11,0)
        self.ui.layout.addWidget(self.ui.label_ligne_qrcode,12,0)
        
       
        self.ui.layout.addWidget(self.ui.combo_ville,1,1)
        self.ui.layout.addWidget(self.ui.combo_site,2,1)
        self.ui.layout.addWidget(self.ui.combo_entrepot_physique,3,1)
        self.ui.layout.addWidget(self.ui.input_entrepot_logique,4,1)
        self.ui.layout.addWidget(self.ui.combo_etat,5,1)
        self.ui.layout.addWidget(self.ui.combo_sous_etat,6,1)
        self.ui.layout.addWidget(self.ui.combo_motif,7,1)
        self.ui.layout.addWidget(self.ui.combo_grade,8,1)
        self.ui.layout.addWidget(self.ui.combo_blanchiment,9,1)
        self.ui.layout.addWidget(self.ui.input_compte_gl,10,1)
        self.ui.layout.addWidget(self.ui.input_id_rebut,11,1)
        self.ui.layout.addWidget(self.ui.input_ligne_qrcode,12,1)
        
                
        self.ui.setLayout(self.ui.layout)
        self.show()
 
    def _updateCombo_sous_etat(self, text):
        self.ui.combo_sous_etat.clear()
        if text == "En stock" or text == "En cours de transit":
            self.ui.combo_sous_etat.addItems(("A arbitrer",
                            "A livrer",
                            "A préparer",
                            "A rechercher",
                            "A réinitialiser",
                            "A sortir",
                            "Disponible",
                            "Maintenance IFG",
                            "Maintenance SAV",
                            "Réservé",
                            "Spare"))
        elif text == "En cours d'utilisation":
            self.ui.combo_sous_etat.addItems(("En cours de RETEX","Utilisé"))
    
    def _updateCombo_motif(self, text):
        self.ui.combo_motif.clear()
        if text == "A sortir":
            self.ui.combo_motif.addItems(("A donner",
                                    "A rendre au loueur",
                                    "A vendre",
                                    "A détruire",
                                    "En cours de reprise",
                                    "A rendre Mainteneur"))
        elif text == "Réservé":
            self.ui.combo_motif.addItems(("Opportunité",
                                    "Prêt",
                                    "Projet",
                                    "Revalorisation"))
        else:
            self.ui.combo_motif.addItems(("sans motif",))  
    
    def _updateCombo_site(self, text):
        self.ui.combo_site.clear()
        if text == "Marseille":
            self.ui.combo_site.addItems(("Viton 9",
                                        "Viton 140",
                                        "Allar 7",
                                        ))
            
        elif text == "Montpellier":
            self.ui.combo_site.addItems(("Arion",))
            
        elif text == "Nice":
            self.ui.combo_site.addItems(("Digue des Français",))
            
        elif text == "Cruas":
            self.ui.combo_site.addItems(("CNPE Cruas",))
            
        elif text == "Saint-Paul-Trois-Châteaux":
            self.ui.combo_site.addItems(("CNPE Tricastin",))
            
        elif text == "Lyon":
            self.ui.combo_site.addItems(("Thiers",
                                        "Nova",
                                        "LGH",
                                        ))

        elif text == "Saint-Alban":
            self.ui.combo_site.addItems(("CNPE Saint-Alban",))
            
        elif text == "Bugey":
            self.ui.combo_site.addItems(("CNPE Bugey",))
            
        elif text == "Grenoble":
            self.ui.combo_site.addItems(("ETANG 134",))
            
        elif text == "Chambéry":
            self.ui.combo_site.addItems(("TECHNOLAC",))
  
    def _updateCombo_entrepot_physique(self, text):
        self.ui.combo_entrepot_physique.clear()
        if text == "Viton 140":
            self.ui.combo_entrepot_physique.addItems(("IFG - 13 - VITON 140_BATIMENT MODULAIRE_RDC_ESPACE IT",))
        elif text == "Viton 9":
            self.ui.combo_entrepot_physique.addItems(( "IFG - 13 - VITON 9_BATIMENT_RDC_007 STOCK IFG",
                                        "IFG - 13 - VITON 9_BATIMENT_RDC_009 LABO IFG",
                                        "IFG - 13 - VITON 9_BATIMENT_RDC_018 STOCK RESEAU IFG",
                                        "IFG - 13 - VITON 9_BATIMENT_RDC_024 BIS BUREAU IFG"
                                        ))
        elif text == "Allar 7":
            self.ui.combo_entrepot_physique.addItems(("IFG - 13 - ALLAR 7_BATIMENT ALLAR 1_RDC_ESPACE IT",))
        elif text == "Arion":
            self.ui.combo_entrepot_physique.addItems(("IFG - 34 - ARION_BATIMENT_2 ETG AILE EST_LOCAL STOCK",))
        elif text == "Digue des Français":
            self.ui.combo_entrepot_physique.addItems(("IFG - 06 - DIGUE DES FRANCAIS 515_BATIMENT_RDC_LOCAL SI",))
        elif text == "CNPE Cruas":
            self.ui.combo_entrepot_physique.addItems(("IFG - 07 - CRUAS RN 86_BAT. DIRECTION_SS 1_BG111",
                                        "IFG - 07 - CRUAS RN 86_BAT. DIRECTION_SS 1_BG115",
                                        "IFG - 07 - CRUAS RN 86_BAT. DIRECTION_SS 1_STOCK BANDOTHEQUE ECONOCOM",
                                        "IFG - 07 - CRUAS RN 86_BAT. GULI_1 ETG_ESPACE IT",
                                        ))
        elif text == "CNPE Tricastin":
            self.ui.combo_entrepot_physique.addItems(("IFG - 26 - TRICASTIN_BATIMENT E_RDC_E0082 ESPACE IT",
                                        "IFG - 26 - TRICASTIN_BATIMENT SUD_1 ETG_S1037",
                                        "IFG - 26 - TRICASTIN_BATIMENT SUD_1 ETG_S1091",
                                        "IFG - 26 - TRICASTIN_BATIMENT SUD_1 ETG_S1098",
                                        "IFG - 26 - TRICASTIN_BATIMENT SUD_1 ETG_S1111",
                                        ))
        elif text == "Thiers":
            self.ui.combo_entrepot_physique.addItems(("IFG - 69 - THIERS LYON 06_BATIMENT_RDC_AILE A_BUREAUX",
                                        "IFG - 69 - THIERS LYON 06_BATIMENT_RDC_AILE A_LABO",
                                        "IFG - 69 - THIERS LYON 06_BATIMENT_RDC_AILE A_STOCK",
                                        ))
        elif text == "Nova":
            self.ui.combo_entrepot_physique.addItems(("IFG - 69 - FOUQUE 5_BATIMENT NOVA_1 ETG_ESPACE IT",))
        elif text == "LGH":
            self.ui.combo_entrepot_physique.addItems(("IFG - 69 - BOURDEIX 19_BATIMENT NORD_RDC_00.NE.08",))   
        elif text == "CNPE Saint-Alban":
            self.ui.combo_entrepot_physique.addItems(("IFG - 38 - SAINT ALBAN_BES_1 ETG_BES 0627",
                                        "IFG - 38 - SAINT ALBAN_BES_RDC_BES 0535",
                                        "IFG - 38 - SAINT ALBAN_BES_SS 1_BA 04 12 (SALLE TELECOM)",
                                        "IFG - 38 - SAINT ALBAN_PILAT_2 ETG_ESPACE IT",
                                        ))
        elif text == "CNPE Bugey":
            self.ui.combo_entrepot_physique.addItems(("IFG - 01 - CAMP LA VALBONNE_BAT. 36_RDC_36C006 ESPACE IT",
                                        "IFG - 01 - CAMP LA VALBONNE_BAT. 36_RDC_36D002",
                                        "IFG - 01 - SAINT VULBAS_BAT. 02_RDC_2008",
                                        ))
        elif text == "ETANG 134":
            self.ui.combo_entrepot_physique.addItems(("IFG - 38 - ETANG 134_BATIMENT PH3_1 ETG_LOCAL INFOGERANT",))
        elif text == "TECHNOLAC":
            self.ui.combo_entrepot_physique.addItems(("IFG - 73 - TECHNOLAC_CENTAURE_RDC AILE BELLEDONNE_BUREAU INFOGERANT",))


    def _updateLineText(self,text):
        text
        self.ui.input_ligne_qrcode.clear()
        self.ui.input_ligne_qrcode.setText(text)
   
            
if __name__== '__main__':
    app = QtWidgets.QApplication([])
    gui = Main(app)
    sys.exit(app.exec_())
