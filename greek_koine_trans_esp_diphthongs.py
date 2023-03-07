import libs.greek_lib as greeklib
import json 

#diphthong (αι)
file_diphthong1 = open('words_diphthongs/diphthong_αι.json', encoding="utf8")   
greeks1 = json.load(file_diphthong1)

#diphthong (ει)
file_diphthong2 = open('words_diphthongs/diphthong_ει.json', encoding="utf8")   
greeks2 = json.load(file_diphthong2)

#diphthong (οι)
file_diphthong3 = open('words_diphthongs/diphthong_οι.json', encoding="utf8")   
greeks3 = json.load(file_diphthong3)

#diphthong (ιο, ιε) antecedido por consonantes sonoras (β,γ,δ,ζ,λ,μ,ν,ρ)
file_diphthong4 = open('words_diphthongs/diphthong_ιο_ιε.json', encoding="utf8")   
greeks4 = json.load(file_diphthong4)

#diphthong (αυ, ευ) antecedido por consonantes sonoras (β,γ,δ,ζ,λ,μ,ν,ρ)
file_diphthong5 = open('words_diphthongs/diphthong_αυ_ευ_sonoras.json', encoding="utf8")   
greeks5 = json.load(file_diphthong5)

#diphthong (αυ, ευ) antecedido por consonantes sordas (κ,π,τ,φ,χ,θ,σ,ξ,ψ)
file_diphthong6 = open('words_diphthongs/diphthong_αυ_ευ_sordas.json', encoding="utf8")   
greeks6 = json.load(file_diphthong6)

#diphthong (ει, ου)
file_diphthong7 = open('words_diphthongs/diphthong_ει_ου.json', encoding="utf8")   
greeks7 = json.load(file_diphthong7)

#diphthong mix
file_diphthong8 = open('words_diphthongs/diphthong_mix.json', encoding="utf8")   
greeks8 = json.load(file_diphthong8)

greeklib.word_details(greeks1, False)
        

