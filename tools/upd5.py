"""Repositionnement : mise à niveau digitale, bilan gratuit, packs S/M/L, entretien 79, heure 110."""
import re, os, sys
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site', 'index.html')
h = open(p, encoding='utf-8').read()

def rep(old, new):
    global h
    assert old in h, 'MISSING: ' + old[:90]
    h = h.replace(old, new, 1)

def sub_between(start, end, new):
    """replace from start marker (inclusive) to end marker (exclusive)"""
    global h
    i = h.index(start); j = h.index(end, i)
    h = h[:i] + new + h[j:]

# ---------------- CSS ----------------
rep('.list{width:100%;', '.pricing2{display:grid;grid-template-columns:1fr 1.15fr;gap:20px;margin-top:20px;align-items:start}@media (max-width:1000px){.pricing2{grid-template-columns:1fr}}.plan .price.range{font-size:2.05rem}.plan h3{margin:0}\n.list{width:100%;')

# ---------------- Meta ----------------
h = re.sub(r'<meta name="description" content="[^"]*">',
  '<meta name="description" content="Atelier Remaster : la mise à niveau digitale des petites entreprises établies. Logo, site, réseaux et présence en ligne : bilan gratuit et plan sur mesure. Bienne.">', h, 1)
h = h.replace('<meta property="og:description" content="Votre image, remise à neuf. Sans perdre ce qui vous rend reconnaissable.">',
  '<meta property="og:description" content="La mise à niveau digitale de votre entreprise : bilan gratuit, plan sur mesure, prix fixe.">')

# ---------------- Hero ----------------
rep('<span data-i="h1a">Votre image, remise à jour.</span> <span class="quiet" data-i="h1b">Sans perdre ce qui vous fait reconnaître.</span>',
    '<span data-i="h1a">La mise à niveau digitale de votre entreprise.</span> <span class="quiet" data-i="h1b">Sans perdre ce qui vous fait reconnaître.</span>')
h = re.sub(r'<p class="lead" data-i="lead">.*?</p>',
  '<p class="lead" data-i="lead">Du logo au site, des réseaux sociaux aux e-mails : nous faisons le bilan de tout ce qui compose votre image en ligne. Vous recevez un plan de remise à niveau sur mesure, avec un prix fixe. Puis nous nous occupons de tout.</p>', h, count=1, flags=re.S)
rep('<p class="small" data-i="small">Le bilan et les premières pistes sont gratuits et sans engagement.</p>',
    '<p class="small" data-i="small">Le bilan et le plan chiffré sont gratuits et sans engagement.</p>')
rep('Nous vérifions pour vous ce qu\'un nouveau client voit en premier, et vous recevez le bilan sous trois jours ouvrés.',
    'Nous analysons ce qu\'un nouveau client voit en premier, et vous recevez le bilan avec un plan de remise à niveau chiffré, sous trois jours ouvrables.')
sub_between('<li data-i="ck1">', '</ul>',
  '<li data-i="ck1">Votre logo et votre identité visuelle</li>\n'
  '          <li data-i="ck2">Votre site, sur ordinateur et sur téléphone</li>\n'
  '          <li data-i="ck3">La sécurité de votre site et de vos e-mails</li>\n'
  '          <li data-i="ck4">Vos réseaux sociaux</li>\n'
  '          <li data-i="ck5">Votre présence sur Google</li>\n'
  '          <li data-i="ck6">La cohérence de votre image d\'un support à l\'autre</li>\n        ')
rep("Merci, c'est bien reçu. Votre bilan vous parvient par e-mail dans les trois jours ouvrables.",
    "Merci, c'est bien reçu. Votre bilan et votre plan vous parviennent par e-mail dans les trois jours ouvrables.")

# ---------------- Prestations ----------------
rep('<p class="lead" data-i="w_l">Quatre domaines, faits sérieusement, pour des entreprises qui ont mieux à faire que leur marketing.</p>',
    '<p class="lead" data-i="w_l">Une remise à niveau complète, du logo au site, pour des entreprises qui ont mieux à faire que leur marketing.</p>')
rep('<h3 data-i="w2t">Tenir votre présence en ligne</h3>', '<h3 data-i="w2t">Un site moderne et sûr</h3>')
h = re.sub(r'<p data-i="w2p">.*?</p>',
  '<p data-i="w2p">Clair, rapide, lisible sur téléphone, en français et en allemand si besoin. Hébergé, sécurisé et tenu à jour par nos soins. Votre fiche Google suit, au passage.</p>', h, count=1, flags=re.S)

# ---------------- Méthode ----------------
sub_between('<div class="steps">', '</div>\n  </div>\n</section>\n\n<section id="tarifs">',
  '<div class="steps">\n'
  '      <div class="step"><div class="num">1</div><h3 data-i="m1t">Nous faisons le bilan</h3><p data-i="m1p">Gratuitement. Logo, site, réseaux, Google, e-mails : nous regardons tout, avec les yeux d\'un nouveau client.</p></div>\n'
  '      <div class="step"><div class="num">2</div><h3 data-i="m2t">Vous recevez un plan chiffré</h3><p data-i="m2p">Ce qu\'il faut faire, dans quel ordre, et pour quel prix fixe. On en parle une demi-heure en visioconférence, vous décidez.</p></div>\n'
  '      <div class="step"><div class="num">3</div><h3 data-i="m3t">On s\'occupe de tout</h3><p data-i="m3p">Vous validez chaque étape. Ensuite, un message ou une photo suffit pour toute nouvelle demande.</p></div>\n    ')

# ---------------- Tarifs ----------------
NEW_T = '''<section id="tarifs">
  <div class="wrap">
    <h2 data-i="p_t">Des prix clairs, fixés avant de commencer</h2>
    <p class="lead" data-i="p_l">Le bilan est gratuit. Il débouche sur un plan sur mesure et un prix fixe, que vous validez avant tout travail. Prix en CHF, hors TVA.</p>
    <div class="pricing">
      <div class="plan">
        <span class="who" data-i="s_w">Rafraîchir</span>
        <h3>Pack S</h3>
        <div class="price range">1'800–3'000</div>
        <ul>
          <li data-i="s1">Logo retouché et mis au propre</li>
          <li data-i="s2">Site existant corrigé, ou nouvelle page unique</li>
          <li data-i="s3">Profils Google et réseaux remis à neuf</li>
          <li data-i="s4">Fichiers prêts pour tous les supports</li>
        </ul>
        <p class="terms" data-i="s_t">Pour une image correcte, mais qui a pris de l'âge.</p>
      </div>
      <div class="plan feature">
        <span class="who" data-i="m_w">Remettre à niveau</span>
        <h3>Pack M</h3>
        <div class="price range">4'000–7'000</div>
        <ul>
          <li data-i="mm1">Logo modernisé et identité visuelle complète</li>
          <li data-i="mm2">Site vitrine neuf, rapide et sécurisé</li>
          <li data-i="mm3">Google et deux réseaux sociaux configurés</li>
          <li data-i="mm4">Modèles : papeterie, signature e-mail, publications</li>
        </ul>
        <p class="terms" data-i="m_tt">Le cas le plus fréquent.</p>
      </div>
      <div class="plan">
        <span class="who" data-i="l_w">Refondre</span>
        <h3>Pack L</h3>
        <div class="price range"><small data-i="from">dès</small> 8'000</div>
        <ul>
          <li data-i="l1">Nouvelle identité visuelle complète</li>
          <li data-i="l2">Site de plusieurs pages, en français et en allemand</li>
          <li data-i="l3">Rédaction de tous les contenus</li>
          <li data-i="l4">Plan de communication pour l'année</li>
        </ul>
        <p class="terms" data-i="l_t">Quand tout est à reprendre.</p>
      </div>
    </div>
    <div class="pricing2">
      <div class="plan">
        <span class="who" data-i="e_w">Après la mise à niveau</span>
        <h3 data-i="e_h">Entretien</h3>
        <div class="price">79.– <small data-i="pm">par mois</small></div>
        <ul>
          <li data-i="e1">Hébergement, sécurité et certificat du site</li>
          <li data-i="e2">Petites mises à jour du site, jusqu'à 30 minutes par mois</li>
          <li data-i="e3">Surveillance de votre présence en ligne, avec nos propositions</li>
          <li data-i="e4">Un point avec vous chaque trimestre</li>
        </ul>
        <p class="terms" data-i="e_t">Six mois minimum, puis résiliable chaque mois.</p>
      </div>
      <div class="plan">
        <span class="who" data-i="al_w">À la pièce, sans engagement</span>
        <table class="list">
          <tr><td data-i="a0">Heure de travail, au quart d'heure</td><td>110</td></tr>
          <tr><td data-i="a4">Affiche, flyer, annonce ou carte</td><td>90</td></tr>
          <tr><td data-i="a5">Publication sur les réseaux</td><td>60</td></tr>
          <tr><td data-i="a6">Annonce d'emploi</td><td>180</td></tr>
          <tr><td data-i="a5c">Campagne sponsorisée, mise en place et suivi (hors budget publicitaire)</td><td>250</td></tr>
        </table>
      </div>
    </div>
    <p class="fict" data-i="p_terms">Le prix exact de votre pack figure dans votre plan, avant tout engagement. Aucun dépassement sans votre accord. Vos fichiers vous appartiennent.</p>
  </div>
</section>
'''
sub_between('<section id="tarifs">', '<section>\n  <div class="wrap">\n    <h2 data-i="g_t">', NEW_T + '\n')

# ---------------- Why us tweaks ----------------
h = re.sub(r'<p data-i="g1p">.*?</p>', '<p data-i="g1p">Le bilan et le plan sont gratuits. Vous ne payez que ce que vous validez, au prix annoncé.</p>', h, count=1, flags=re.S)
h = re.sub(r'<p data-i="g3p">.*?</p>', '<p data-i="g3p">Un prix fixe par projet. L\'entretien est résiliable chaque mois après six mois. Rien de plus.</p>', h, count=1, flags=re.S)
h = re.sub(r'<p data-i="g8p">.*?</p>', '<p data-i="g8p">Un horaire à corriger, une saison qui approche, une page qui vieillit : on vous le signale avec une proposition.</p>', h, count=1, flags=re.S)

# ---------------- FAQ ----------------
h = re.sub(r'\s*<details><summary data-i="f3q">.*?</details>', '', h, count=1, flags=re.S)
h = re.sub(r'\s*<details><summary data-i="f4q">.*?</details>', '', h, count=1, flags=re.S)
rep('<details><summary data-i="f6q">',
    '<details><summary data-i="f7q">Combien coûte une mise à niveau ?</summary><p data-i="f7a">Cela dépend de ce que le bilan révèle. La plupart des entreprises se situent dans le Pack M, entre 4\'000 et 7\'000 francs. Le prix exact figure dans votre plan, et il ne bouge plus une fois validé.</p></details>\n'
    '      <details><summary data-i="f8q">Et après la mise à niveau ?</summary><p data-i="f8a">Avec l\'entretien à 79 francs par mois, votre site reste à jour et sécurisé, et nous gardons un œil sur votre présence en ligne. Pour le reste, vous commandez à la pièce, quand vous en avez besoin.</p></details>\n'
    '      <details><summary data-i="f6q">')

# ---------------- JS: drop calculator ----------------
sub_between('/* calculator */\nconst P=', '/* forms -> FormSubmit', "let LANG='fr';\nfunction calc(){}\n\n")

# ---------------- German ----------------
DE = {
 'h1a': 'Die digitale Auffrischung Ihres Unternehmens.',
 'lead': 'Vom Logo zur Website, von den sozialen Medien bis zu den E-Mails: Wir analysieren alles, was Ihr Bild im Internet ausmacht. Sie erhalten einen massgeschneiderten Plan mit Fixpreis. Danach kümmern wir uns um alles.',
 'small': 'Analyse und Plan mit Preis sind kostenlos und unverbindlich.',
 'ck_l': 'Nennen Sie uns Ihr Unternehmen. Wir prüfen, was ein neuer Kunde zuerst sieht, und Sie erhalten die Analyse mit einem bezifferten Plan innert drei Arbeitstagen.',
 'ck1': 'Ihr Logo und Ihr visueller Auftritt', 'ck2': 'Ihre Website, am Computer und auf dem Handy',
 'ck3': 'Die Sicherheit Ihrer Website und Ihrer E-Mails', 'ck4': 'Ihre sozialen Medien',
 'ck5': 'Ihre Präsenz auf Google', 'ck6': 'Ein einheitlicher Auftritt auf allen Kanälen',
 'b_ok': 'Danke, Ihre Anfrage ist eingegangen. Analyse und Plan erhalten Sie innert drei Arbeitstagen per E-Mail.',
 'w_l': 'Eine vollständige Auffrischung, vom Logo bis zur Website, für Unternehmen, die Besseres zu tun haben als Marketing.',
 'w2t': 'Eine moderne, sichere Website',
 'w2p': 'Klar, schnell, auf dem Handy lesbar, bei Bedarf auf Deutsch und Französisch. Von uns gehostet, gesichert und aktuell gehalten. Ihr Google-Eintrag gleich mit.',
 'm1t': 'Wir machen die Analyse', 'm1p': 'Kostenlos. Logo, Website, soziale Medien, Google, E-Mails: Wir schauen alles an, mit den Augen eines neuen Kunden.',
 'm2t': 'Sie erhalten einen bezifferten Plan', 'm2p': 'Was zu tun ist, in welcher Reihenfolge und zu welchem Fixpreis. Wir besprechen ihn eine halbe Stunde per Videocall, Sie entscheiden.',
 'm3t': 'Wir kümmern uns um alles', 'm3p': 'Sie geben jeden Schritt frei. Danach genügt eine Nachricht oder ein Foto für jede neue Anfrage.',
 'p_t': 'Klare Preise, festgelegt vor dem Start', 'p_l': 'Die Analyse ist kostenlos. Daraus entsteht ein massgeschneiderter Plan mit Fixpreis, den Sie vor Arbeitsbeginn freigeben. Preise in CHF, exkl. MWST.',
 's_w': 'Auffrischen', 's1': 'Logo überarbeitet und bereinigt', 's2': 'Bestehende Website korrigiert oder neue One-Page', 's3': 'Google- und Social-Media-Profile erneuert', 's4': 'Dateien für alle Anwendungen', 's_t': 'Für einen soliden Auftritt, der in die Jahre gekommen ist.',
 'm_w': 'Auf den neusten Stand bringen', 'mm1': 'Logo modernisiert und vollständiger visueller Auftritt', 'mm2': 'Neue Website, schnell und sicher', 'mm3': 'Google und zwei soziale Netzwerke eingerichtet', 'mm4': 'Vorlagen: Geschäftspapier, E-Mail-Signatur, Beiträge', 'm_tt': 'Der häufigste Fall.',
 'l_w': 'Neu aufbauen', 'from': 'ab', 'l1': 'Komplett neuer visueller Auftritt', 'l2': 'Website mit mehreren Seiten, auf Deutsch und Französisch', 'l3': 'Alle Inhalte getextet', 'l4': 'Kommunikationsplan für das ganze Jahr', 'l_t': 'Wenn alles neu gemacht werden muss.',
 'e_w': 'Nach der Auffrischung', 'e_h': 'Betreuung', 'pm': 'pro Monat',
 'e1': 'Hosting, Sicherheit und Zertifikat der Website', 'e2': 'Kleine Website-Anpassungen, bis 30 Minuten pro Monat', 'e3': 'Überwachung Ihrer Online-Präsenz, mit unseren Vorschlägen', 'e4': 'Ein Gespräch mit Ihnen pro Quartal', 'e_t': 'Mindestens sechs Monate, danach monatlich kündbar.',
 'al_w': 'Einzeln, ohne Verpflichtung', 'a0': 'Arbeitsstunde, pro Viertelstunde verrechnet', 'a4': 'Plakat, Flyer, Inserat oder Karte',
 'p_terms': 'Der genaue Preis Ihres Pakets steht in Ihrem Plan, vor jeder Verpflichtung. Keine Mehrkosten ohne Ihre Zustimmung. Ihre Dateien gehören Ihnen.',
 'g1p': 'Analyse und Plan sind kostenlos. Sie zahlen nur, was Sie freigeben, zum angekündigten Preis.',
 'g3p': 'Ein Fixpreis pro Projekt. Die Betreuung ist nach sechs Monaten monatlich kündbar. Mehr nicht.',
 'g8p': 'Falsche Öffnungszeiten, eine nahende Saison, eine Seite, die altert: Wir melden es Ihnen mit einem Vorschlag.',
 'f7q': 'Was kostet eine Auffrischung?', 'f7a': 'Das hängt davon ab, was die Analyse zeigt. Die meisten Unternehmen liegen im Paket M, zwischen 4\'000 und 7\'000 Franken. Der genaue Preis steht in Ihrem Plan und ändert sich nach der Freigabe nicht mehr.',
 'f8q': 'Und nach der Auffrischung?', 'f8a': 'Mit der Betreuung für 79 Franken pro Monat bleibt Ihre Website aktuell und sicher, und wir behalten Ihre Online-Präsenz im Auge. Alles andere bestellen Sie einzeln, wenn Sie es brauchen.',
}
import json
js = 'Object.assign(DE,' + json.dumps(DE, ensure_ascii=False) + ');\n'
rep('const FR={};', js + 'const FR={};')

open(p, 'w', encoding='utf-8').write(h)
print('ok')
