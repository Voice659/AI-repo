import random, math, datetime

def planet_weight(weight_kg):
    factors = {"Mercury": 0.38, "Venus": 0.91, "Mars": 0.38, "Jupiter": 2.34, "Saturn": 1.06, "Uranus": 0.92, "Neptune": 1.19, "Moon": 0.165, "Sun": 27.9}
    results = []
    for p, f in factors.items():
        results.append("{}: {:.1f} kg".format(p, weight_kg * f))
    return "\n".join(results)

def solar_system_age(earth_years):
    ratios = {"Mercury": 0.241, "Venus": 0.615, "Mars": 1.881, "Jupiter": 11.86, "Saturn": 29.46, "Uranus": 84.01, "Neptune": 164.8}
    results = []
    for p, r in ratios.items():
        results.append("{}: {:.2f} years".format(p, earth_years / r))
    return "\n".join(results)

def space_distance_scale():
    items = [
        ("Earth to Moon", 384400, "km"),
        ("Earth to Sun", 149.6e6, "km"),
        ("Sun to Mars", 227.9e6, "km"),
        ("Sun to Jupiter", 778.6e6, "km"),
        ("Sun to Saturn", 1.43e9, "km"),
        ("Sun to Neptune", 4.5e9, "km"),
        ("Sun to Proxima Centauri", 4.24, "light years"),
        ("Milky Way diameter", 100000, "light years"),
        ("Andromeda distance", 2.537e6, "light years"),
        ("Observable universe", 93e9, "light years"),
    ]
    return "\n".join("{}: {:.2e} {}".format(n, d, u) for n, d, u in items)

def apollo_missions():
    missions = [
        ("Apollo 1", "1967", "Capsule fire during test", "Failed"),
        ("Apollo 7", "1968", "First crewed Apollo flight", "Success"),
        ("Apollo 8", "1968", "First humans to orbit the Moon", "Success"),
        ("Apollo 9", "1969", "Earth orbit LM test", "Success"),
        ("Apollo 10", "1969", "Dress rehearsal for Moon landing", "Success"),
        ("Apollo 11", "1969", "First Moon landing", "Success"),
        ("Apollo 12", "1969", "Second Moon landing", "Success"),
        ("Apollo 13", "1970", "Oxygen tank explosion, aborted", "Partial"),
        ("Apollo 14", "1971", "Third Moon landing", "Success"),
        ("Apollo 15", "1971", "First lunar rover", "Success"),
        ("Apollo 16", "1972", "Fifth Moon landing", "Success"),
        ("Apollo 17", "1972", "Last Moon landing", "Success"),
    ]
    info = random.choice(missions)
    return "{} ({}): {} - {}".format(*info)

def rocket_facts():
    facts = [
        "The Saturn V remains the most powerful rocket ever built.",
        "SpaceX's Falcon 9 is the first reusable orbital rocket.",
        "The Space Shuttle had 135 missions total.",
        "The first rocket to reach space was V-2 in 1944.",
        "The fastest spacecraft is the Parker Solar Probe at 700,000 km/h.",
        "The Saturn V had 5 F-1 engines each burning 2.8 tons of fuel per second.",
        "The Falcon Heavy can lift 64 tons to low Earth orbit.",
        "The Starship is designed to carry 100 people to Mars.",
        "The Soyuz rocket is the most launched rocket in history.",
        "The Delta IV Heavy is the largest rocket in US service.",
        "The Ariane 5 has launched over 100 missions for Europe.",
        "The Long March 5 is China's heavy lift rocket.",
        "The Electron rocket is made mostly of carbon fiber.",
        "The New Shepard is a suborbital tourist rocket.",
        "The SLS is NASA's next heavy lift rocket for Artemis.",
    ]
    return random.choice(facts)

def mars_facts():
    facts = [
        "Mars is 227.9 million km from the Sun.",
        "A day on Mars is 24.6 hours (sol).",
        "A year on Mars is 687 Earth days.",
        "Mars has two moons: Phobos and Deimos.",
        "The gravity on Mars is 38% of Earth's.",
        "Mars has the tallest mountain: Olympus Mons at 21.9 km.",
        "Mars has the longest canyon: Valles Marineris at 4,000 km.",
        "The atmosphere is 95% carbon dioxide.",
        "Mars has four seasons like Earth but twice as long.",
        "Temperatures range from -140C to 20C.",
        "Mars has polar ice caps made of water and CO2.",
        "The first successful Mars rover was Sojourner in 1997.",
        "The Perseverance rover landed in 2021.",
        "NASA plans to send humans to Mars in the 2030s.",
        "There is water ice on Mars.",
    ]
    return random.choice(facts)

def jupiter_facts():
    facts = [
        "Jupiter is the largest planet at 142,984 km diameter.",
        "Jupiter has the shortest day at 9.9 hours.",
        "Jupiter has 95 known moons.",
        "The Great Red Spot is a storm larger than Earth.",
        "Jupiter's magnetic field is 14 times stronger than Earth's.",
        "Jupiter has rings, but they are faint.",
        "The atmosphere is mostly hydrogen and helium.",
        "Jupiter's mass is 2.5 times all other planets combined.",
        "The temperature at cloud tops is -145C.",
        "Jupiter has a rocky core maybe 20 times Earth's mass.",
        "Europa, a moon of Jupiter, may have an ocean.",
        "Io has the most volcanic activity in the solar system.",
        "Ganymede is the largest moon in the solar system.",
        "Callisto has the oldest surface in the solar system.",
        "The Juno spacecraft has been orbiting Jupiter since 2016.",
    ]
    return random.choice(facts)

def deep_space_fact():
    facts = [
        "The Boomerang Nebula is the coldest place at -272C.",
        "The largest known star is UY Scuti with radius 1,700 times the Sun.",
        "The fastest rotating star spins at 2 million km/h.",
        "The most massive known star is R136a1 at 265 solar masses.",
        "The oldest known star is Methuselah at 14.5 billion years.",
        "The nearest black hole is 1,500 light years away.",
        "The largest known black hole has 40 billion solar masses.",
        "The most luminous known quasar shines 600 trillion times brighter than the Sun.",
        "The most distant galaxy is 13.4 billion light years away.",
        "The largest known structure is the Hercules-Corona Borealis Great Wall.",
        "There are an estimated 2 trillion galaxies in the observable universe.",
        "The cosmic microwave background radiation is 2.7 Kelvin.",
        "The first stars formed 100 million years after the Big Bang.",
        "The universe is expanding at 67 km/s per megaparsec.",
        "Dark energy constitutes 68% of the universe's energy density.",
    ]
    return random.choice(facts)

def random_moon():
    moons = [
        "Moon (Earth)", "Phobos (Mars)", "Deimos (Mars)", "Io (Jupiter)", "Europa (Jupiter)",
        "Ganymede (Jupiter)", "Callisto (Jupiter)", "Titan (Saturn)", "Enceladus (Saturn)",
        "Mimas (Saturn)", "Tethys (Saturn)", "Dione (Saturn)", "Rhea (Saturn)",
        "Iapetus (Saturn)", "Phoebe (Saturn)", "Hyperion (Saturn)", "Miranda (Uranus)",
        "Ariel (Uranus)", "Umbriel (Uranus)", "Titania (Uranus)", "Oberon (Uranus)",
        "Triton (Neptune)", "Nereid (Neptune)", "Proteus (Neptune)", "Charon (Pluto)",
        "Nix (Pluto)", "Hydra (Pluto)", "Kerberos (Pluto)", "Styx (Pluto)",
        "Deimos (Mars)", "Phobos (Mars)",
    ]
    return random.choice(moons)

def random_exoplanet():
    planets = [
        "Proxima Centauri b", "TRAPPIST-1e", "Kepler-452b", "HD 209458b (Osiris)",
        "51 Pegasi b", "Kepler-16b", "GJ 1214b", "HD 189733b",
        "Kepler-22b", "Kepler-69c", "Kepler-186f", "Kepler-442b",
        "Kepler-452b", "Kepler-62f", "Kepler-10b", "WASP-12b",
        "K2-18b", "TOI-700d", "LHS 1140b", "GJ 357 d",
        "HD 219134b", "Gl 581 g", "HD 40307 g", "Kepler-438b",
    ]
    return random.choice(planets)

def astronauts_on_iss():
    return "Currently there are usually 7 astronauts on the ISS from the US, Russia, Japan, and Europe."

def speed_of_light_travel(distance_ly):
    return "It would take {:.2f} years traveling at light speed.".format(distance_ly)

def asteroid_belt_fact():
    facts = [
        "The asteroid belt lies between Mars and Jupiter.",
        "Ceres is the largest asteroid at 940 km diameter.",
        "There are over 1 million asteroids larger than 1 km.",
        "The total mass of the belt is only 4% of the Moon.",
        "Asteroids are leftovers from the solar system's formation.",
        "The first asteroid discovered was Ceres in 1801.",
        "Vesta has a mountain taller than Everest.",
        "Some asteroids have their own moons.",
        "The Chicxulub impactor was 10 km wide.",
        "NASA's OSIRIS-REx collected samples from Bennu.",
        "Japan's Hayabusa2 collected samples from Ryugu.",
        "The Psyche mission will visit a metal asteroid.",
        "Most asteroids are irregularly shaped.",
        "Trojan asteroids share Jupiter's orbit.",
        "Near-Earth asteroids are tracked for planetary defense.",
    ]
    return random.choice(facts)
