import locale

def proper_diphthongs(greek, spanish):
    new_spanish = ''
    if greek.find("αι") >= 0:
        new_spanish = spanish.replace("ai","e")
        print("Diptongo (αι): "+new_spanish)
        print("----------------------------------------------")
    if greek.find("ει") >= 0:
        new_spanish = spanish.replace("ei","i")
        print("Diptongo (ει): "+new_spanish)
        print("----------------------------------------------")
    if greek.find("οι") >= 0:
        new_spanish = spanish.replace("oi","i")
        print("Diptongo (οι): "+new_spanish)
        print("----------------------------------------------")
    if greek.find("ου") >= 0:
        new_spanish = spanish.replace("ou","u")
        print("Diptongo (ου): "+new_spanish)
        print("----------------------------------------------")
    if greek.find("υι") >= 0:
        new_spanish = spanish.replace("ui","i")
        print("Diptongo (υι): "+new_spanish)
        print("----------------------------------------------")
    if greek.find("αυβ") >= 0 or greek.find("αυγ") >= 0 or greek.find("αυδ") >= 0 or greek.find("αυζ") >= 0 or greek.find("αυλ") >= 0 or greek.find("αυμ") >= 0 or greek.find("αυν") >= 0 or greek.find("αυρ") >= 0:
        new_spanish = spanish.replace("au","av")
        print("Diptongo (αυ): "+new_spanish)
        print("antecedido por consonantes sonoras (β,γ,δ,ζ,λ,μ,ν,ρ)")
        print("----------------------------------------------")
    if greek.find("ευα") >= 0 or greek.find("ευε") >= 0 or greek.find("ευη") >= 0 or greek.find("ευι") >= 0 or greek.find("ευο") >= 0 or greek.find("ευυ") >= 0 or greek.find("ευω") >= 0:
        new_spanish = spanish.replace("eu","ev")
        print("Diptongo (ευ): "+new_spanish)
        print("antecedido por vocales (α,ε,η,ι,ο,υ,ω)")
        print("----------------------------------------------")
    if greek.find("αυα") >= 0 or greek.find("αυε") >= 0 or greek.find("αυη") >= 0 or greek.find("αυι") >= 0 or greek.find("αυο") >= 0 or greek.find("αυυ") >= 0 or greek.find("αυω") >= 0:
        new_spanish = spanish.replace("au","av")
        print("Diptongo (αυ): "+new_spanish)
        print("antecedido por vocales (α,ε,η,ι,ο,υ,ω)")
        print("----------------------------------------------")
    if greek.find("ευβ") >= 0 or greek.find("ευγ") >= 0 or greek.find("ευδ") >= 0 or greek.find("ευζ") >= 0 or greek.find("ευλ") >= 0 or greek.find("ευμ") >= 0 or greek.find("ευν") >= 0 or greek.find("ευρ") >= 0:
        new_spanish = spanish.replace("eu","ev")
        print("Diptongo (ευ): "+new_spanish)
        print("antecedido por consonantes sonoras (β,γ,δ,ζ,λ,μ,ν,ρ)")
        print("----------------------------------------------")
    if greek.find("αυκ") >= 0 or greek.find("αυπ") >= 0 or greek.find("αυτ") >= 0 or greek.find("αυφ") >= 0 or greek.find("αυχ") >= 0:
        new_spanish = spanish.replace("au","af")
        print("Diptongo (αυ): "+new_spanish)
        print("antecedido por consonantes sordas (κ,π,τ,φ,χ,θ,σ,ξ,ψ)")
        print("----------------------------------------------")
    if greek.find("αυθ") >= 0 or greek.find("αυσ") >= 0 or greek.find("αυς") >= 0 or greek.find("αυξ") >= 0 or greek.find("αυψ") >= 0:
        new_spanish = spanish.replace("au","af")
        print("Diptongo (αυ): "+new_spanish)
        print("antecedido por consonantes sordas (κ,π,τ,φ,χ,θ,σ,ξ,ψ)")
        print("----------------------------------------------")
    if greek.find("ευκ") >= 0 or greek.find("ευπ") >= 0 or greek.find("ευτ") >= 0 or greek.find("ευφ") >= 0 or greek.find("ευχ") >= 0:
        new_spanish = spanish.replace("eu","ef")
        print("Diptongo (ευ): "+new_spanish)
        print("antecedido por consonantes sordas (κ,π,τ,φ,χ,θ,σ,ξ,ψ)")
        print("----------------------------------------------")
    if greek.find("ευθ") >= 0 or greek.find("ευσ") >= 0 or greek.find("ευς") >= 0 or greek.find("ευξ") >= 0 or greek.find("ευψ") >= 0:
        new_spanish = spanish.replace("eu","ef")
        print("Diptongo (ευ): "+new_spanish)
        print("antecedido por consonantes sordas (κ,π,τ,φ,χ,θ,σ,ξ,ψ)")
        print("----------------------------------------------")
    if greek.find("ηυβ") >= 0 or greek.find("ηυγ") >= 0 or greek.find("ηυδ") >= 0 or greek.find("ηυζ") >= 0 or greek.find("ηυλ") >= 0 or greek.find("ηυμ") >= 0 or greek.find("ηυν") >= 0 or greek.find("ηυρ") >= 0:
        new_spanish = spanish.replace("iu","iv")
        print("Diptongo (ηυ): "+new_spanish)
        print("antecedido por consonantes sonoras (β,γ,δ,ζ,λ,μ,ν,ρ)")
        print("----------------------------------------------")
    if greek.find("ηυκ") >= 0 or greek.find("ηυπ") >= 0 or greek.find("ηυτ") >= 0 or greek.find("ηυφ") >= 0 or greek.find("ηυχ") >= 0 or greek.find("ηυθ") >= 0 or greek.find("ηυσ") >= 0 or greek.find("ηυξ") >= 0 or greek.find("ηυψ") >= 0:
        new_spanish = spanish.replace("iu","if")
        print("Diptongo (ηυ): "+new_spanish)
        print("antecedido por consonantes sordas (κ,π,τ,φ,χ,θ,σ,ξ,ψ)")
        print("----------------------------------------------")


def equivalencies():
    return [('Α','α','a','913','945','Alpha'),
            ('Β','β','b','914','946','Beta'),
            ('Γ','γ','g','915','947','Gamma'),
            ('Δ','δ','d','916','948','Delta'),
            ('Ε','ε','e','917','949','Épsilon'),
            ('Ζ','ζ','z','918','950','Zeta'),
            ('Η','η','ẽ','919','951','Eta'),
            ('Θ','θ','th','920','952','Theta'),
            ('Ι','ι','i','921','953','Iota'),
            ('Κ','κ','k','922','954','Kappa'),
            ('Λ','λ','l','923','955','Lambda'),
            ('Μ','μ','m','924','956','Mu'),
            ('Ν','ν','n','925','957','Nu'),
            ('Ξ','ξ','x','926','958','Xi'),
            ('Ο','ο','o','927','959','Ómicron'),
            ('Ο','ό','o','927','959','Ómicron'),
            ('Π','π','p','928','960','Pi'),
            ('Ρ','ρ','r','929','961','Rho'),
            ('Σ','σ','s','931','963','Sigma'),
            ('Σ','ς','s','931','962','Sigma'), 
            ('Τ','τ','t','932','964','Tau'),
            ('Υ','υ','u','933','965','Upsilon'),
            ('Υ','ύ','u','933','965','Upsilon'),
            ('Φ','φ','f','934','966','Phi'),
            ('Χ','χ','j','935','967','Ji'),
            ('Ψ','ψ','ps','936','968','Psi'),
            ('Ω','ω','o','937','969','Omega')]


def equivalencies_without_sigma():
    return [('Α','α','a','913','945','Alpha'),
            ('Β','β','b','914','946','Beta'),
            ('Γ','γ','g','915','947','Gamma'),
            ('Δ','δ','d','916','948','Delta'),
            ('Ε','ε','e','917','949','Épsilon'),
            ('Ζ','ζ','z','918','950','Zeta'),
            ('Η','η','ẽ','919','951','Eta'),
            ('Θ','θ','th','920','952','Theta'),
            ('Ι','ι','i','921','953','Iota'),
            ('Κ','κ','k','922','954','Kappa'),
            ('Λ','λ','l','923','955','Lambda'),
            ('Μ','μ','m','924','956','Mu'),
            ('Ν','ν','n','925','957','Nu'),
            ('Ξ','ξ','x','926','958','Xi'),
            ('Ο','ο','o','927','959','Ómicron'),
            ('Π','π','p','928','960','Pi'),
            ('Ρ','ρ','r','929','961','Rho'),
            ('Σ','σ','s','931','963','Sigma'),
            ('Τ','τ','t','932','964','Tau'),
            ('Υ','υ','u','933','965','Upsilon'),
            ('Φ','φ','f','934','966','Phi'),
            ('Χ','χ','j','935','967','Ji'),
            ('Ψ','ψ','ps','936','968','Psi'),
            ('Ω','ω','õ','937','969','Omega')]
    
def count_s(strvar):
    counter = 0
    result = []
    for i in strvar:
        if i == 's':
            result.append(counter)
        counter = counter + 1
    return result

def sigma_case(word, greek, details):
    count_pos = count_s(word)
    if len(count_s(word)) >= 2:
        max_item = max(count_pos, key=int)
        new_greek = [i for i in greek]
        new_greek[max_item] = 'ς'
        greek = "".join(new_greek)
        details[max_item][1] = 'ς'
    return [greek, details]

#order words
def order_words(words):
    locale.setlocale(locale.LC_ALL, 'el_GR.UTF-8')
    words_ordered = sorted(words.keys(), key=locale.strxfrm)
    count = 1
    for word in words_ordered:
        print(str(count)+" : "+word+" - "+words[word])
        count = count + 1

#Show word details
def word_details(greeks, flag_details):
    for greek in greeks.keys():
        spanish = ""
        details = []
        for char in greek:
            for equiv in equivalencies():
                if char.lower() in equiv:
                    details.append([char, equiv[2], equiv[5]])
                    spanish = spanish + equiv[2]

        if greek != "":
                    
            if flag_details:
                print("----------------------------------------------")
                print("Detalles de Transliteración: ")
                print("----------------------------------------------")

                for val in details:
                    print(val[0]+' : '+val[1]+' : '+val[2])

            print("----------------------------------------------")
            print("Palabra (Griego Koiné): "+greek)
            print("Palabra (Español): "+greeks[greek])
            print("Palabra (Transliteración): "+spanish)
            proper_diphthongs(greek.lower(), spanish.lower())