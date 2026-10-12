"""Je au lieu de nous, H1 court, multilingue, réseaux = mise en place du système, photo."""
import re, os, json
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
p = os.path.join(R, 'index.html')
h = open(p, encoding='utf-8').read()

def set_fr(key, text):
    """replace inner HTML of the element carrying data-i=key"""
    global h
    pat = re.compile(r'(data-i="%s"[^>]*>)(.*?)(</)' % re.escape(key), re.S)
    assert pat.search(h), 'missing key ' + key
    h = pat.sub(lambda m: m.group(1) + text + m.group(3), h, count=1)

def rep(old, new):
    global h
    assert old in h, 'MISSING: ' + old[:80]
    h = h.replace(old, new, 1)

# ---- H1: shorter, no second line
rep('<span data-i="h1a">La mise à niveau digitale de votre entreprise.</span> <span class="quiet" data-i="h1b">Sans perdre ce qui vous fait reconnaître.</span>',
    '<span data-i="h1a">Votre entreprise, mise à niveau.</span>')

FR = {
 'lead': "Logo, site, réseaux sociaux, e-mails : je fais le bilan de tout ce qui compose votre image en ligne. Vous recevez un plan sur mesure à prix fixe, puis je m'occupe de tout.",
 'cta1': 'Mes prestations',
 'ck_l': "Indiquez votre entreprise. J'analyse ce qu'un nouveau client voit en premier, et vous recevez le bilan avec un plan de remise à niveau chiffré, sous trois jours ouvrables.",
 'w_t': 'Ce que je fais pour vous',
 'w1p': "Logo, couleurs, papeterie, modèles de documents. Je garde votre nom, votre couleur, votre histoire, et je rends le tout lisible partout, de l'enseigne à l'écran du téléphone.",
 'w2p': "Clair, rapide, lisible sur téléphone, dans toutes les langues de vos clients. Hébergé, sécurisé et tenu à jour par mes soins. Votre fiche Google suit, au passage.",
 'w4t': 'Mettre en place vos réseaux sociaux',
 'w4p': "Instagram, Facebook, LinkedIn. Profils soignés, modèles de publication à vos couleurs, planning et outils pour publier en quelques minutes. Je mets le système en place, vous publiez en toute autonomie.",
 'm1t': 'Je fais le bilan',
 'm1p': "Gratuitement. Logo, site, réseaux, Google, e-mails : je regarde tout, avec les yeux d'un nouveau client.",
 'm2p': "Ce qu'il faut faire, dans quel ordre, et pour quel prix fixe. On en parle une demi-heure en visioconférence, vous décidez.",
 'm3t': "Je m'occupe de tout",
 'mm3': 'Google et deux réseaux sociaux mis en place, avec modèles de publication',
 'mm4': 'Modèles : papeterie, signature e-mail, documents',
 'l2': 'Site de plusieurs pages, multilingue',
 'e3': 'Surveillance de votre présence en ligne, avec mes propositions',
 'g_t': 'Pourquoi travailler avec moi',
 'g_l': "Vous dirigez votre entreprise. Je fais le travail de marketing, vous gardez les décisions.",
 'g7p': "Je fais les analyses et je vous propose ce qui convient à votre entreprise. Vous dites oui, non ou « plutôt comme ça ».",
 'g8p': "Un horaire à corriger, une saison qui approche, une page qui vieillit : je vous le signale avec une proposition.",
 'g4p': "Une seule personne qui connaît votre entreprise, en français, en allemand et en anglais.",
 'f1a': "Justement parce qu'ils le connaissent. Je garde ce qu'ils reconnaissent (le nom, la couleur, le signe) et je le rends lisible là où on vous découvre aujourd'hui : sur Google, sur un téléphone, dans un onglet. Si rien ne doit changer, je vous le dirai.",
 'f2a': "Non. On commence par le numérique (site, Google, e-mails), puis le reste suit au rythme de vos renouvellements naturels. Je vous remets un plan simple.",
 'f8a': "Avec l'entretien à 79 francs par mois, votre site reste à jour et sécurisé, et je garde un œil sur votre présence en ligne. Pour le reste, vous commandez à la pièce, quand vous en avez besoin.",
 'f6q': 'Publiez-vous sur nos réseaux à notre place ?',
 'f6a': "Non, et c'est voulu : personne ne connaît votre quotidien mieux que vous. Je mets en place tout le système (profils, modèles, planning, outils) et je vous montre comment publier en quelques minutes. Si vous voulez de l'aide ponctuelle, elle se commande à la pièce.",
 'f5q': 'Travaillez-vous en plusieurs langues ?',
 'f5a': "Oui. Français, allemand et anglais, rédigés pour chaque langue et non traduits mot à mot. D'autres langues sont possibles sur demande.",
}
for k, v in FR.items():
    set_fr(k, v)

# à la pièce: replace "Publication sur les réseaux" by a set-up item
rep('<tr><td data-i="a5">Publication sur les réseaux</td><td>60</td></tr>',
    '<tr><td data-i="a5">Modèle de publication réutilisable</td><td>60</td></tr>')

# ---- Photo in contact block
rep('<p class="big">Julien Dornbierer</p>',
    '<img class="portrait" src="img/julien.jpg" width="112" height="112" alt="Julien Dornbierer" loading="lazy">\n        <p class="big">Julien Dornbierer</p>')
rep('.list{width:100%;', '.portrait{width:112px;height:112px;border-radius:50%;object-fit:cover;display:block;margin-bottom:14px;background:var(--mist)}\n.list{width:100%;')

# ---- Meta
h = re.sub(r'<meta name="description" content="[^"]*">',
  '<meta name="description" content="Atelier Remaster : la mise à niveau digitale des petites entreprises établies. Logo, site, réseaux et présence en ligne : bilan gratuit et plan sur mesure. Julien Dornbierer, Bienne.">', h, count=1)

# ---- German overrides (appended after previous Object.assign, so they win)
DE = {
 'h1a': 'Ihr Unternehmen, auf den neusten Stand.',
 'lead': 'Logo, Website, soziale Medien, E-Mails: Ich analysiere alles, was Ihr Bild im Internet ausmacht. Sie erhalten einen massgeschneiderten Plan mit Fixpreis, danach kümmere ich mich um alles.',
 'cta1': 'Meine Leistungen',
 'ck_l': 'Nennen Sie mir Ihr Unternehmen. Ich prüfe, was ein neuer Kunde zuerst sieht, und Sie erhalten die Analyse mit einem bezifferten Plan innert drei Arbeitstagen.',
 'w_t': 'Was ich für Sie tue',
 'w1p': 'Logo, Farben, Geschäftspapier, Dokumentvorlagen. Ich behalte Ihren Namen, Ihre Farbe, Ihre Geschichte und mache alles überall lesbar, vom Firmenschild bis zum Handy.',
 'w2p': 'Klar, schnell, auf dem Handy lesbar, in allen Sprachen Ihrer Kunden. Von mir gehostet, gesichert und aktuell gehalten. Ihr Google-Eintrag gleich mit.',
 'w4t': 'Ihre sozialen Medien einrichten',
 'w4p': 'Instagram, Facebook, LinkedIn. Gepflegte Profile, Beitragsvorlagen in Ihren Farben, Planung und Werkzeuge, um in wenigen Minuten zu posten. Ich richte das System ein, Sie veröffentlichen selbständig.',
 'm1t': 'Ich mache die Analyse',
 'm1p': 'Kostenlos. Logo, Website, soziale Medien, Google, E-Mails: Ich schaue alles an, mit den Augen eines neuen Kunden.',
 'm2p': 'Was zu tun ist, in welcher Reihenfolge und zu welchem Fixpreis. Wir besprechen ihn eine halbe Stunde per Videocall, Sie entscheiden.',
 'm3t': 'Ich kümmere mich um alles',
 'mm3': 'Google und zwei soziale Netzwerke eingerichtet, mit Beitragsvorlagen',
 'mm4': 'Vorlagen: Geschäftspapier, E-Mail-Signatur, Dokumente',
 'l2': 'Website mit mehreren Seiten, mehrsprachig',
 'e3': 'Überwachung Ihrer Online-Präsenz, mit meinen Vorschlägen',
 'a5': 'Wiederverwendbare Beitragsvorlage',
 'g_t': 'Warum mit mir arbeiten',
 'g_l': 'Sie führen Ihr Unternehmen. Ich erledige das Marketing, Sie behalten die Entscheide.',
 'g7p': 'Ich mache die Analysen und schlage vor, was zu Ihrem Unternehmen passt. Sie sagen ja, nein oder «eher so».',
 'g8p': 'Falsche Öffnungszeiten, eine nahende Saison, eine Seite, die altert: Ich melde es Ihnen mit einem Vorschlag.',
 'g4p': 'Eine Person, die Ihr Unternehmen kennt, auf Deutsch, Französisch und Englisch.',
 'f1a': 'Gerade weil sie es kennen. Was sie wiedererkennen (Name, Farbe, Zeichen), bleibt, und ich mache es dort lesbar, wo man Sie heute entdeckt: auf Google, auf dem Handy, im Browser. Wenn nichts geändert werden muss, sage ich es Ihnen.',
 'f2a': 'Nein. Wir beginnen mit dem Digitalen (Website, Google, E-Mails), der Rest folgt im Rhythmus Ihrer natürlichen Erneuerungen. Ich gebe Ihnen einen einfachen Plan.',
 'f8a': 'Mit der Betreuung für 79 Franken pro Monat bleibt Ihre Website aktuell und sicher, und ich behalte Ihre Online-Präsenz im Auge. Alles andere bestellen Sie einzeln, wenn Sie es brauchen.',
 'f6q': 'Posten Sie für uns auf unseren Kanälen?',
 'f6a': 'Nein, und das ist Absicht: Niemand kennt Ihren Alltag besser als Sie. Ich richte das ganze System ein (Profile, Vorlagen, Planung, Werkzeuge) und zeige Ihnen, wie Sie in wenigen Minuten posten. Punktuelle Hilfe können Sie einzeln bestellen.',
 'f5q': 'Arbeiten Sie in mehreren Sprachen?',
 'f5a': 'Ja. Deutsch, Französisch und Englisch, für jede Sprache geschrieben, nicht Wort für Wort übersetzt. Weitere Sprachen auf Anfrage.',
 'k_l': 'Nennen Sie mir Ihr Unternehmen. Sie erhalten eine Skizze mit Ihrem eigenen Logo, kostenlos und unverbindlich.',
}
rep('const FR={};', 'Object.assign(DE,' + json.dumps(DE, ensure_ascii=False) + ');\nconst FR={};')
open(p, 'w', encoding='utf-8').write(h)

# ---- Legal page: je
lp = os.path.join(R, 'mentions-legales.html')
L = open(lp, encoding='utf-8').read()
for a, b in [
  ("à notre boîte e-mail, gérée par Google Workspace", "à ma boîte e-mail, gérée par Google Workspace"),
  ("Nous utilisons ces données uniquement", "J'utilise ces données uniquement"),
  ("an unser E-Mail-Postfach bei Google Workspace", "an mein E-Mail-Postfach bei Google Workspace"),
  ("Wir verwenden die Daten ausschliesslich", "Ich verwende die Daten ausschliesslich"),
]:
    assert a in L, a
    L = L.replace(a, b)
open(lp, 'w', encoding='utf-8').write(L)
print('ok')
