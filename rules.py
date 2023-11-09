import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Definisi variabel fuzzy
kecepatan_mobil = ctrl.Antecedent(np.arange(0, 120, 1), 'kecepatan_mobil')
jarak = ctrl.Antecedent(np.arange(0, 20, 1), 'jarak')
beban = ctrl.Antecedent(np.arange(10, 1750, 1), 'beban')
putaran_roda = ctrl.Consequent(np.arange(0, 750, 1), 'putaran_roda')
daya_cengkram_rem = ctrl.Consequent(np.arange(0, 4495, 1), 'daya_cengkram_rem')
# kelembapan = ctrl.Antecedent(np.arange(15, 50, 1), 'kelembapan')

kecepatan_mobil['pelan'] = fuzz.trimf(kecepatan_mobil.universe, [0, 0, 40])
kecepatan_mobil['cukup_pelan'] = fuzz.trimf(kecepatan_mobil.universe, [20, 40, 60])
kecepatan_mobil['sedang'] = fuzz.trimf(kecepatan_mobil.universe, [40, 60, 80])
kecepatan_mobil['cukup_cepat'] = fuzz.trimf(kecepatan_mobil.universe, [60, 80, 100])
kecepatan_mobil['cepat'] = fuzz.trimf(kecepatan_mobil.universe, [80, 100, 120])
# print("kecepatan_mobil", kecepatan_mobil.universe)

jarak['sangat_dekat'] = fuzz.trimf(jarak.universe, [0, 0, 11])
jarak['dekat'] = fuzz.trimf(jarak.universe, [8, 11, 14])
jarak['sedang'] = fuzz.trimf(jarak.universe, [11, 14, 17])
jarak['jauh'] = fuzz.trimf(jarak.universe, [14, 17, 20])
# jarak['jauh'] = fuzz.trimf(jarak.universe, [80, 100, 120])
# print("jarak", jarak.universe)

beban['ringan'] = fuzz.trimf(beban.universe, [0, 0, 750])
beban['sedang'] = fuzz.trimf(beban.universe, [500, 750, 1000])
beban['berat'] = fuzz.trimf(beban.universe, [1000, 1250, 1500])
beban['sangat_berat'] = fuzz.trimf(beban.universe, [1250, 1500, 1750])
# print("beban", beban.universe)

# kelembapan['low'] = fuzz.trimf(kelembapan.universe, [0, 0, 20])
# kelembapan['medium'] = fuzz.trimf(kelembapan.universe, [10, 20, 30])
# kelembapan['high'] = fuzz.trimf(kelembapan.universe, [30, 40, 50])
# print("kelembapan", kelembapan.universe)

putaran_roda['minimum'] = fuzz.trimf(putaran_roda.universe, [0, 0, 350])
putaran_roda['slow'] = fuzz.trimf(putaran_roda.universe, [250, 350, 450])
putaran_roda['medium'] = fuzz.trimf(putaran_roda.universe, [350, 450, 550])
putaran_roda['fast'] = fuzz.trimf(putaran_roda.universe, [450, 550, 650])
putaran_roda['maximum'] = fuzz.trimf(putaran_roda.universe, [550, 650, 750])
# print("putaran_roda", putaran_roda.universe)

daya_cengkram_rem['minimum'] = fuzz.trimf(daya_cengkram_rem.universe, [0, 0, 2895])
daya_cengkram_rem['slow'] = fuzz.trimf(daya_cengkram_rem.universe, [2495, 2895, 3295])
daya_cengkram_rem['medium'] = fuzz.trimf(daya_cengkram_rem.universe, [2895, 3295, 3695])
daya_cengkram_rem['hard'] = fuzz.trimf(daya_cengkram_rem.universe, [3295, 3695, 4095])
daya_cengkram_rem['maximum'] = fuzz.trimf(daya_cengkram_rem.universe, [3695, 4095, 4495])


# Aturan fuzzy
def get_putaran_roda_control_rules():
    rule1a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        putaran_roda['minimum']
    )
    rule1b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['berat'],
        putaran_roda['minimum']
    )
    rule1c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['sedang'],
        putaran_roda['minimum']
    )
    rule1d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['ringan'],
        putaran_roda['minimum']
    )

    rule2a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        putaran_roda['minimum']
    )
    rule2b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['berat'],
        putaran_roda['minimum']
    )
    rule2c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['sedang'],
        putaran_roda['minimum']
    )
    rule2d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['ringan'],
        putaran_roda['minimum']
    )

    rule3a = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        putaran_roda['minimum']
    )
    rule3b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sangat_dekat'] & beban['berat'],
        putaran_roda['minimum']
    )
    rule3c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sangat_dekat'] & beban['sedang'],
        putaran_roda['minimum']
    )
    rule3d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sangat_dekat'] & beban['ringan'],
        putaran_roda['minimum']
    )

    rule4a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        putaran_roda['minimum']
    )
    rule4b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['berat'],
        putaran_roda['minimum']
    )
    rule4c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['sedang'],
        putaran_roda['minimum']
    )
    rule4d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['ringan'],
        putaran_roda['minimum']
    )

    rule5a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        putaran_roda['minimum']
    )
    rule5b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['berat'],
        putaran_roda['minimum']
    )
    rule5c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['sedang'],
        putaran_roda['minimum']
    )
    rule5d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['ringan'],
        putaran_roda['minimum']
    )

    # ----------------------------------------------------------------------------
    rule6a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule6b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['berat'],
        putaran_roda['slow']
    )
    rule6c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['sedang'],
        putaran_roda['slow']
    )
    rule6d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['ringan'],
        putaran_roda['slow']
    )

    rule7a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule7b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['berat'],
        putaran_roda['slow']
    )
    rule7c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['sedang'],
        putaran_roda['slow']
    )
    rule7d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['ringan'],
        putaran_roda['slow']
    )

    rule8a = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['dekat'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule8b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['dekat'] & beban['berat'],
        putaran_roda['slow']
    )
    rule8c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['dekat'] & beban['sedang'],
        putaran_roda['slow']
    )
    rule8d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['dekat'] & beban['ringan'],
        putaran_roda['slow']
    )

    rule9a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule9b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['berat'],
        putaran_roda['slow']
    )
    rule9c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['sedang'],
        putaran_roda['slow']
    )
    rule9d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['ringan'],
        putaran_roda['slow']
    )

    rule10a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule10b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['berat'],
        putaran_roda['slow']
    )
    rule10c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['sedang'],
        putaran_roda['slow']
    )
    rule10d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['ringan'],
        putaran_roda['slow']
    )

    # ----------------------------------------------------------------------------
    rule11a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule11b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['berat'],
        putaran_roda['medium']
    )
    rule11c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['sedang'],
        putaran_roda['medium']
    )
    rule11d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['ringan'],
        putaran_roda['medium']
    )

    rule12a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule12b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['berat'],
        putaran_roda['medium']
    )
    rule12c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['sedang'],
        putaran_roda['medium']
    )
    rule12d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['ringan'],
        putaran_roda['medium']
    )

    rule13a = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule13b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['berat'],
        putaran_roda['medium']
    )
    rule13c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['sedang'],
        putaran_roda['medium']
    )
    rule13d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['ringan'],
        putaran_roda['medium']
    )

    rule14a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['sangat_berat'],
        putaran_roda['medium']
    )
    rule14b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['berat'],
        putaran_roda['medium']
    )
    rule14c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['sedang'],
        putaran_roda['medium']
    )
    rule14d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['ringan'],
        putaran_roda['medium']
    )

    rule15a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['sangat_berat'],
        putaran_roda['slow']
    )
    rule15b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['berat'],
        putaran_roda['medium']
    )
    rule15c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['sedang'],
        putaran_roda['medium']
    )
    rule15d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['ringan'],
        putaran_roda['medium']
    )

    # ----------------------------------------------------------------------------
    rule16a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['sangat_berat'],
        putaran_roda['medium']
    )
    rule16b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['berat'],
        putaran_roda['fast']
    )
    rule16c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['sedang'],
        putaran_roda['fast']
    )
    rule16d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['ringan'],
        putaran_roda['fast']
    )

    rule17a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['sangat_berat'],
        putaran_roda['medium']
    )
    rule17b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['berat'],
        putaran_roda['fast']
    )
    rule17c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['sedang'],
        putaran_roda['fast']
    )
    rule17d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['ringan'],
        putaran_roda['fast']
    )

    rule18a = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['sangat_berat'],
        putaran_roda['medium']
    )
    rule18b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['berat'],
        putaran_roda['fast']
    )
    rule18c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['sedang'],
        putaran_roda['fast']
    )
    rule18d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['ringan'],
        putaran_roda['fast']
    )

    rule19a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['sangat_berat'],
        putaran_roda['medium']
    )
    rule19b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['berat'],
        putaran_roda['fast']
    )
    rule19c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['sedang'],
        putaran_roda['fast']
    )
    rule19d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['ringan'],
        putaran_roda['fast']
    )

    rule20a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['sangat_berat'],
        putaran_roda['medium']
    )
    rule20b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['berat'],
        putaran_roda['fast']
    )
    rule20c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['sedang'],
        putaran_roda['fast']
    )
    rule20d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['ringan'],
        putaran_roda['fast']
    )


    return [
        rule1a, rule1b, rule1c, rule1d,
        rule2a, rule2b, rule2c, rule2d,
        rule3a, rule3b, rule3c, rule3d,
        rule4a, rule4b, rule4c, rule4d,
        rule5a, rule5b, rule5c, rule5d,

        rule6a, rule6b, rule6c, rule6d,
        rule7a, rule7b, rule7c, rule7d,
        rule8a, rule8b, rule8c, rule8d,
        rule9a, rule9b, rule9c, rule9d,
        rule10a, rule10b, rule10c, rule10d,

        rule11a, rule11b, rule11c, rule11d,
        rule12a, rule12b, rule12c, rule12d,
        rule13a, rule13b, rule13c, rule13d,
        rule14a, rule14b, rule14c, rule14d,
        rule15a, rule15b, rule15c, rule15d,

        rule16a, rule16b, rule16c, rule16d,
        rule17a, rule17b, rule17c, rule17d,
        rule18a, rule18b, rule18c, rule18d,
        rule19a, rule19b, rule19c, rule19d,
        rule20a, rule20b, rule20c, rule20d
    ]


def get_daya_cengkram_rem_control_rules():
    rule1a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule1b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['berat'],
        daya_cengkram_rem['maximum']
    )
    rule1c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['sedang'],
        daya_cengkram_rem['maximum']
    )
    rule1d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sangat_dekat'] & beban['ringan'],
        daya_cengkram_rem['maximum']
    )

    rule2a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule2b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['berat'],
        daya_cengkram_rem['maximum']
    )
    rule2c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['sedang'],
        daya_cengkram_rem['maximum']
    )
    rule2d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['ringan'],
        daya_cengkram_rem['maximum']
    )

    rule3a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule3b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sangat_dekat'] & beban['berat'],
        daya_cengkram_rem['maximum']
    )
    rule3c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sangat_dekat'] & beban['sedang'],
        daya_cengkram_rem['maximum']
    )
    rule3d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sangat_dekat'] & beban['ringan'],
        daya_cengkram_rem['maximum']
    )

    rule4a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule4b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['berat'],
        daya_cengkram_rem['maximum']
    )
    rule4c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['sedang'],
        daya_cengkram_rem['maximum']
    )
    rule4d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sangat_dekat'] & beban['ringan'],
        daya_cengkram_rem['maximum']
    )

    rule5a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['hard']
    )
    rule5b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['berat'],
        daya_cengkram_rem['hard']
    )
    rule5c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['sedang'],
        daya_cengkram_rem['hard']
    )
    rule5d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sangat_dekat'] & beban['ringan'],
        daya_cengkram_rem['hard']
    )

    # ----------------------------------------------------------------------------
    rule6a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule6b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['berat'],
        daya_cengkram_rem['hard']
    )
    rule6c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['sedang'],
        daya_cengkram_rem['hard']
    )
    rule6d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['dekat'] & beban['ringan'],
        daya_cengkram_rem['hard']
    )

    rule7a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule7b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['berat'],
        daya_cengkram_rem['hard']
    )
    rule7c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['sedang'],
        daya_cengkram_rem['hard']
    )
    rule7d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['ringan'],
        daya_cengkram_rem['hard']
    )

    rule8a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule8b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['dekat'] & beban['berat'],
        daya_cengkram_rem['hard']
    )
    rule8c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['dekat'] & beban['sedang'],
        daya_cengkram_rem['hard']
    )
    rule8d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['dekat'] & beban['ringan'],
        daya_cengkram_rem['hard']
    )

    rule9a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['maximum']
    )
    rule9b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['berat'],
        daya_cengkram_rem['hard']
    )
    rule9c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['sedang'],
        daya_cengkram_rem['hard']
    )
    rule9d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['dekat'] & beban['ringan'],
        daya_cengkram_rem['hard']
    )

    rule10a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['sangat_berat'],
        daya_cengkram_rem['hard']
    )
    rule10b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['berat'],
        daya_cengkram_rem['medium']
    )
    rule10c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['sedang'],
        daya_cengkram_rem['medium']
    )
    rule10d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['dekat'] & beban['ringan'],
        daya_cengkram_rem['medium']
    )

    # ----------------------------------------------------------------------------
    rule11a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['sangat_berat'],
        daya_cengkram_rem['hard']
    )
    rule11b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['berat'],
        daya_cengkram_rem['hard']
    )
    rule11c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['sedang'],
        daya_cengkram_rem['medium']
    )
    rule11d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['sedang'] & beban['ringan'],
        daya_cengkram_rem['medium']
    )

    rule12a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['sangat_berat'],
        daya_cengkram_rem['hard']
    )
    rule12b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['berat'],
        daya_cengkram_rem['hard']
    )
    rule12c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['sedang'],
        daya_cengkram_rem['medium']
    )
    rule12d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['sedang'] & beban['ringan'],
        daya_cengkram_rem['medium']
    )

    rule13a = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['sangat_berat'],
        daya_cengkram_rem['medium']
    )
    rule13b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['berat'],
        daya_cengkram_rem['medium']
    )
    rule13c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['sedang'],
        daya_cengkram_rem['slow']
    )
    rule13d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['sedang'] & beban['ringan'],
        daya_cengkram_rem['slow']
    )

    rule14a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['sangat_berat'],
        daya_cengkram_rem['medium']
    )
    rule14b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['berat'],
        daya_cengkram_rem['medium']
    )
    rule14c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['sedang'],
        daya_cengkram_rem['slow']
    )
    rule14d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['sedang'] & beban['ringan'],
        daya_cengkram_rem['slow']
    )

    rule15a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['sangat_berat'],
        daya_cengkram_rem['medium']
    )
    rule15b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['berat'],
        daya_cengkram_rem['slow']
    )
    rule15c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['sedang'],
        daya_cengkram_rem['slow']
    )
    rule15d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['sedang'] & beban['ringan'],
        daya_cengkram_rem['slow']
    )

    # ----------------------------------------------------------------------------
    rule16a = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['sangat_berat'],
        daya_cengkram_rem['hard']
    )
    rule16b = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['berat'],
        daya_cengkram_rem['medium']
    )
    rule16c = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['sedang'],
        daya_cengkram_rem['medium']
    )
    rule16d = ctrl.Rule(
        kecepatan_mobil['cepat'] & jarak['jauh'] & beban['ringan'],
        daya_cengkram_rem['medium']
    )

    rule17a = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['sangat_berat'],
        daya_cengkram_rem['hard']
    )
    rule17b = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['berat'],
        daya_cengkram_rem['medium']
    )
    rule17c = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['sedang'],
        daya_cengkram_rem['medium']
    )
    rule17d = ctrl.Rule(
        kecepatan_mobil['cukup_cepat'] & jarak['jauh'] & beban['ringan'],
        daya_cengkram_rem['medium']
    )

    rule18a = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['sangat_berat'],
        daya_cengkram_rem['medium']
    )
    rule18b = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['berat'],
        daya_cengkram_rem['medium']
    )
    rule18c = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['sedang'],
        daya_cengkram_rem['slow']
    )
    rule18d = ctrl.Rule(
        kecepatan_mobil['sedang'] & jarak['jauh'] & beban['ringan'],
        daya_cengkram_rem['slow']
    )

    rule19a = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['sangat_berat'],
        daya_cengkram_rem['medium']
    )
    rule19b = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['berat'],
        daya_cengkram_rem['slow']
    )
    rule19c = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['sedang'],
        daya_cengkram_rem['slow']
    )
    rule19d = ctrl.Rule(
        kecepatan_mobil['cukup_pelan'] & jarak['jauh'] & beban['ringan'],
        daya_cengkram_rem['slow']
    )

    rule20a = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['sangat_berat'],
        daya_cengkram_rem['slow']
    )
    rule20b = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['berat'],
        daya_cengkram_rem['minimum']
    )
    rule20c = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['sedang'],
        daya_cengkram_rem['minimum']
    )
    rule20d = ctrl.Rule(
        kecepatan_mobil['pelan'] & jarak['jauh'] & beban['ringan'],
        daya_cengkram_rem['minimum']
    )


    return [
        rule1a, rule1b, rule1c, rule1d,
        rule2a, rule2b, rule2c, rule2d,
        rule3a, rule3b, rule3c, rule3d,
        rule4a, rule4b, rule4c, rule4d,
        rule5a, rule5b, rule5c, rule5d,

        rule6a, rule6b, rule6c, rule6d,
        rule7a, rule7b, rule7c, rule7d,
        rule8a, rule8b, rule8c, rule8d,
        rule9a, rule9b, rule9c, rule9d,
        rule10a, rule10b, rule10c, rule10d,

        rule11a, rule11b, rule11c, rule11d,
        rule12a, rule12b, rule12c, rule12d,
        rule13a, rule13b, rule13c, rule13d,
        rule14a, rule14b, rule14c, rule14d,
        rule15a, rule15b, rule15c, rule15d,

        rule16a, rule16b, rule16c, rule16d,
        rule17a, rule17b, rule17c, rule17d,
        rule18a, rule18b, rule18c, rule18d,
        rule19a, rule19b, rule19c, rule19d,
        rule20a, rule20b, rule20c, rule20d
    ]