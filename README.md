# proba_tecnica_Data_Science
Es tracta d'una proba tècnica solicitada per IT Academy de Barcelona Activa

Objectius generals:
    1. Analitzar les principals tendències de la ciutat des de la perspectiva del teixit comercial.
        ◦ La meva proposta: Analitzar la distribució i tipologia dels establiments comercials a la ciutat per entendre les tendències actuals (per exemple, quins sectors estan més actius, quins es mantenen estables, quins estan en declivi). Utilitzar tècniques d’anàlisi descriptiva per establir les tendències.
        ◦ Procediment: Necessitem explorar les variables com el tipus d’activitat, el grup d’activitat, la distribució territorial dels establiments i les tendències en relació a les ubicacions (p. ex., concentració a barris o districtes). Una anàlisi exploratòria i la visualització dels canvis al llarg del temps ajudaran a identificar les tendències.
          
    2. Conèixer la vitalitat de la salut comercial i restauració.
        ◦ La meva primera proposta: Si el dataframe ho permet, mesurar la vitalitat comercial mitjançant l'anàlisi de les taxes d’activitat (actiu/inactiu) i les categories d'activitat. Utilitzar mètodes descriptius (com les taules de contingència) per a l'anàlisi del nombre d'establiments en funcionament i la seva evolució.
        ◦ Procediment: A més de la descripció de l'estat dels locals (actiu, buit, etc.), seria interessant introduir una variable de "salut comercial" que mesuri l'activitat i l'estabilitat de cada local. Aquest indicador es podria basar en la freqüència d'activitat comercial o el nombre de locals inactius o en venda.
          
    3. Inspirar en la formulació de polítiques.
        ◦ La meva proposta: Utilitzar les dades per identificar zones amb alta concentració de certs tipus d'establiments (per exemple, restauració vs comerç minorista) i zones amb un gran nombre de locals inactius per a determinar polítiques d’urbanisme i suport a l’activitat comercial.
        ◦ Procediment: A través de les prediccions,identificar quins barris tenen més possibilitats de mantenir o perdre activitat comercial i la necessitat de redissenyar estratègies comercials o urbanístiques (com incentivar certs tipus d’activitats o reconvertir locals).
Objectiu concret: 
Estudi dels locals comercials a Barcelona amb algoritmes de classificació supervisada i anàlisis descriptives per monitoritzar la situació i l’evolució de la salut comercial.
    1. Mesurar i  predir l’evolució de certs indicadors econòmics com si un local estarà actiu, buit o amb una activitat específica.
        ◦ La meva proposta: Ús de modelització predictiva per predir l'estat de l'activitat (actiu, buit, etc.) basant-me en factors com la ubicació, tipus d’activitat, i altres característiques socioeconòmiques.
        ◦ Implementació concreta: Utilitzar Logaritmes de Regressió logistica, Random Forest o XGBoost o altres models de classificació supervisada per predir l'estat d’un local (actiu, buit, amb un tipus d’activitat determinat) en funció de e les condicions dels establiments comercials.
Objectius futurs:
    2. Comparatives amb bases de dades d'altres anys per veure'n l’evolució, tenint en compte canvis sociopolítics i demogràfics. Utilitzar tècniques de regressió i models predictius per identificar factors clau de canvi i correlacionar-los amb canvis externs. Això ens permetria mesurar l'impacte de situacions com la pandèmia en el teixit comercial.
Procediment
    1. Anàlisi descriptiva i exploratòria (EDA) de les tendències comercials a la ciutat.
        ◦ Obtenir una visió general de les dades i assegurar-nos que estan netes i preparades per a l’anàlisi.
        ◦ Llistar les columnes i veure el tipus de dada de cadascuna per identificar si hi ha dades categòriques, numèriques, binàries, objecte, etc.
        ◦ Comprovar si hi ha valors nuls o duplicats que puguin afectar l’anàlisi i gestionar-los adequadament.
        ◦ Realitzar estadístiques descriptives bàsiques
       
    2. Modelització predictiva per classificar els establiments en funció de la seva activitat (actiu, buit, tipus d'activitat).
        ◦ Distribució dels Locals per Categoria d’activitat, barri o districte, amb gràfics de barres o circulars
        ◦ Identificar les categories d’activitat amb major o menor presència de locals, que poden indicar sectors més o menys desenvolupats.
          
    3. Anàlisi temporal i comparativa per mesurar l’evolució dels establiments.
    4. Distribució Geogràfica dels Locals per analitzar com es distribueixen els locals i tipus d’activitat en l’àmbit geogràfic: barris, eixos comercials, mercats... . Crear un mapa o gràfiques que mostrin la concentració de locals per ubicació i comparar districtes o zones per identificar si hi ha àrees amb més locals comercials i si alguna categoria de negoci té una presència destacada en alguna zona específica.
    5. Anàlisi de la Taxa d’Ocupació: Identificar quants locals es troben operatius vs. desocupats o en transició, calcular la proporció de locals ocupats vs. buits o en transició en cada categoria o ubicació. Explorar si hi ha alguna relació entre la taxa d’ocupació i la ubicació o la categoria de negoci. Això pot ajudar a identificar àrees amb potencial d’expansió o inversió.
    6. Relacions entre Variables: Detectar correlacions entre diferents variables que poden donar lloc a insights interessants. Generar un heatmap de correlació per veure visualment quines variables poden estar més interrelacionades i explorar aquestes relacions més a fons.
    7. Predicció de Tendències Futures (Opcional)
    • Objectiu: Anticipar possibles canvis en el sector. Predir l’evolució del nombre de locals en certes categories o zones. Aplicar models de regressió o tècniques de forecasting per veure cap a on pot anar el sector en els pròxims anys.

Presentació del conjunt de dades
Font: https://opendata-
ajuntament.barcelona.cat/data/es/dataset/cens-locals-planta-baixa-act-economica

1. Estructura del DataFrame
El conjunt de dades consta de 66.088 registres amb 49 columnes. De les columnes disponibles, algunes contenen dades numèriques (bàsicament codis), altres són de tipus objecte (cadenes de text) i també hi ha columnes amb valors nuls.
Cada registre és únic i conté característiques sobretot d'ubicació i d'activitat comercial.
2. Descripció general de les columnes
A continuació, es proporciona una descripció general de les columnes clau i les seves característiques: ID_Global: Identificador únic per cada registre.
ID_Bcn_2016: Identificador de l'activitat a la ciutat de Barcelona (algunes files tenen valors nuls).
Codi_Principal_Activitat, Codi_Sector_Activitat, Codi_Grup_Activitat, Codi_Activitat_2022: Còdigs que identifiquen la categoria i subcategoria de l'activitat econòmica del local. Aquests valors són numèrics i els agruparem per analitzar l'activitat comercial.
Nom_Principal_Activitat, Nom_Sector_Activitat, Nom_Grup_Activitat, Nom_Activitat: Noms que descriuen les activitats comercials i el seu sector. Són columnes de tipus objecte (cadenes de text).
Coordenades geogràfiques (Latitud, Longitud): Permeten la geolocalització dels establiments.
Ubicació (Codi_Via, Nom_Via, Codi_Barri, Nom_Barri, Codi_Districte, Nom_Districte): Dades sobre la localització i districte del local. Altres dades de localització i estructurals (Planta, Porta, Num_Policia_Inicial, Num_Policia_Final): Dades relacionades amb la localització específica del local dins de l'edifici i la seva identificació legal.
Tipus d'establiment (p. ex., SN_Oci_Nocturn, SN_Coworking, SN_Servei_Degustacio): Dades categòriques per identificar si un local té característiques especials (oci nocturn, coworking, etc.).
3. Estadístiques Descriptives Generals
Les següents estadístiques es basen en les columnes numèriques de les dades:
ID_Bcn_2016: Els valors de l'ID_Bcn_2016 varien entre 4215 i 78056, però no els utilitzarem degut al gran nombre de valors faltants i ja tenim un altra ID únic.
Coordenades UTM (X_UTM_ETRS89, Y_UTM_ETRS89), Latitud i Longitud: Les coordenades UTM tenen valors molt específics que ajuden a identificar les ubicacions a la ciutat de Barcelona.
Codi_Via i Porta: Aquestes columnes ofereixen la informació sobre les vies i les portes dels locals. Tanmateix, la columna de "Porta" té alguns valors nuls, que gestionarem posteriorment.
Solar, Codi_Parcela, Codi_Illa: Són codis utilitzats per identificar el solar i la parcel·la associada a cada local. Num_Policia_Inicial, Num_Policia_Final: Aquestes columnes mostren els rangs d'adreça per número de policia. ens poden orientar millor que el num porta.
4. Manca de Dades i valors nuls
Algunes columnes contenen valors nuls en una proporció significativa de les files:
Nom_Mercat: Aquesta columna conté només 2.154 valors no nuls, mentre que la resta estan nuls. Això pot indicar que només una part dels establiments estan en mercats.
Nom_Galeria i Nom_CComercial: Similarment, aquestes columnes tenen valors nuls en moltes files, però no necessitem aquestes variables per l'estudi.
Porta, Num_Policia_Inicial, Num_Policia_Final: Algunes d'aquestes dades tenen valors nuls, manca d'una identificació precisa en determinades ubicacions.
El conjunt de dades conté algunes columnes amb una proporció relativament alta de valors nuls. És important netejar o imputar aquests valors abans de continuar amb l'anàlisi. Les columnes s'han de revisar.
5. Tipus de Dades
Dades numèriques: Aquests inclouen les coordenades UTM, latitud, longitud, així com algunes altres dades d’identificació com el Codi_Via.
Dades de text: Els noms de les activitats, sectors, grups d'activitat i altres elements descriptius.
Dades booleanes: Dades com SN_Oci_Nocturn, SN_Coworking, SN_Servei_Degustacio indiquen la presència o absència de característiques específiques dels locals.
