"""Generate data_bulk27.py and data_bulk28.py: 500K+ lines total."""
import random, os

SEED = 2738
random.seed(SEED)

TOPICS27 = [
    "automotive_engine", "transmission_system", "brake_system", "suspension_design", "steering_mechanism",
    "exhaust_system", "fuel_injection", "ignition_system", "cooling_system", "lubrication_system",
    "electric_drivetrain", "regenerative_brake", "battery_pack", "charging_station", "range_estimation",
    "autonomous_driving", "lidar_sensor", "radar_detection", "camera_vision", "ultrasonic_sensor",
    "gps_navigation", "route_planning", "traffic_management", "fleet_optimization", "logistics_network",
    "supply_chain", "warehouse_automation", "inventory_management", "last_mile_delivery", "cargo_tracking",
    "shipping_container", "freight_forwarding", "customs_clearance", "port_operations", "maritime_navigation",
    "aviation_systems", "flight_control", "air_traffic", "runway_safety", "aircraft_maintenance",
    "railroad_signaling", "track_inspection", "train_control", "high_speed_rail", "metro_transit",
    "bicycle_infrastructure", "pedestrian_safety", "road_signage", "traffic_light", "crosswalk_design",
    "parking_system", "toll_collection", "congestion_pricing", "ride_sharing", "car_rental",
    "public_transit", "bus_route", "light_rail", "streetcar_system", "ferry_operation",
    "hyperloop_concept", "maglev_train", "personal_rapid_transit", "drone_delivery", "vertical_takeoff",
    "sports_training", "athletic_performance", "strength_conditioning", "cardio_fitness", "flexibility_training",
    "sports_nutrition", "hydration_strategy", "meal_planning", "supplement_regimen", "recovery_protocol",
    "injury_prevention", "physical_therapy", "sports_medicine", "biomechanics_analysis", "gait_analysis",
    "swing_mechanics", "throwing_mechanics", "jumping_mechanics", "running_form", "swimming_technique",
    "cycling_efficiency", "rowing_stroke", "golf_swing", "tennis_serve", "basketball_shooting",
    "soccer_kicking", "football_tackling", "baseball_pitching", "hockey_shooting", "volleyball_spiking",
    "martial_arts", "boxing_punch", "wrestling_move", "judo_throw", "karate_strike",
    "taekwondo_kick", "jiu_jitsu_submission", "muay_thai_clinch", "krav_maga_defense", "fencing_lunge",
    "yoga_pose", "pilates_exercise", "crossfit_wod", "calisthenics_routine", "bodybuilding_split",
    "weightlifting_form", "powerlifting_technique", "olympic_lift", "kettlebell_swing", "dumbbell_press",
    "barbell_squat", "deadlift_variation", "bench_press", "overhead_press", "barbell_row",
    "pull_up_variation", "push_up_variation", "dip_exercise", "leg_press", "hamstring_curl",
    "quadriceps_extension", "calf_raise", "shoulder_fly", "triceps_pushdown", "bicep_curl",
    "sports_psychology", "mental_toughness", "visualization_technique", "focus_training", "pressure_management",
    "team_dynamics", "leadership_skills", "communication_drill", "conflict_resolution", "goal_setting",
    "competition_strategy", "game_plan", "scouting_report", "opponent_analysis", "performance_analytics",
    "wearable_tech", "heart_rate_monitor", "gps_tracker", "accelerometer_data", "gyroscope_sensor",
    "smart_footwear", "smart_apparel", "impact_sensor", "motion_capture", "video_analysis",
    "esports_training", "reaction_time", "hand_eye_coordination", "strategic_thinking", "team_coordination",
    "racing_line", "pit_stop_strategy", "tire_management", "fuel_strategy", "aerodynamic_drag",
    "downforce_balance", "chassis_setup", "suspension_tuning", "brake_bias", "gear_ratio",
    "drafting_technique", "overtaking_maneuver", "defensive_driving", "corner_entry", "apex_hit",
    "trail_braking", "heel_toe_downshift", "launch_control", "traction_control", "stability_control",
    "abs_braking", "electronic_stability", "torque_vector", "active_suspension", "adaptive_cruise",
    "lane_keeping", "collision_avoidance", "blind_spot_monitor", "driver_alertness", "fatigue_detection",
]
TOPICS28 = [
    "curriculum_design", "lesson_planning", "learning_objective", "assessment_method", "grading_rubric",
    "formative_assessment", "summative_assessment", "standardized_test", "competency_based", "mastery_learning",
    "differentiated_instruction", "classroom_management", "student_engagement", "active_learning", "project_based",
    "inquiry_based", "problem_based", "cooperative_learning", "collaborative_learning", "peer_tutoring",
    "flipped_classroom", "blended_learning", "online_education", "distance_learning", "mooc_course",
    "virtual_classroom", "learning_management", "educational_technology", "adaptive_learning", "personalized_path",
    "early_childhood", "montessori_method", "waldorf_education", "steam_education", "stem_program",
    "literacy_development", "reading_comprehension", "phonics_instruction", "vocabulary_building", "writing_process",
    "numeracy_skills", "mathematical_thinking", "problem_solving", "critical_thinking", "creative_thinking",
    "logic_reasoning", "spatial_awareness", "memory_technique", "mnemonic_device", "study_skill",
    "time_management", "organization_skill", "note_taking", "research_method", "citation_style",
    "academic_writing", "thesis_statement", "argument_construction", "evidence_evaluation", "source_credibility",
    "special_education", "inclusive_classroom", "iep_development", "accommodation_strategy", "behavior_intervention",
    "gifted_education", "enrichment_program", "acceleration_option", "talent_development", "creativity_nurturing",
    "language_acquisition", "second_language", "bilingual_education", "esl_instruction", "immersion_program",
    "adult_education", "continuing_education", "professional_development", "vocational_training", "apprenticeship",
    "corporate_training", "leadership_development", "onboarding_process", "skill_assessment", "competency_mapping",
    "game_design", "level_design", "character_creation", "storytelling_method", "narrative_structure",
    "game_mechanics", "game_balance", "player_progression", "reward_system", "achievement_system",
    "multiplayer_networking", "client_server", "peer_to_peer", "game_physics", "collision_detection",
    "rendering_pipeline", "shader_programming", "lighting_system", "particle_effect", "animation_rigging",
    "sound_design", "music_composition", "voice_acting", "sound_effect", "audio_mixing",
    "user_interface", "hud_design", "menu_navigation", "control_scheme", "accessibility_option",
    "virtual_reality", "augmented_reality", "mixed_reality", "vr_tracking", "hand_gesture",
    "board_game", "card_game", "tabletop_rpg", "miniature_wargame", "strategy_game",
    "puzzle_design", "crossword_construction", "sudoku_generation", "escape_room", "trivia_quiz",
    "role_playing_game", "rpg_mechanics", "stat_system", "skill_tree", "inventory_system",
    "quest_design", "dialogue_system", "faction_reputation", "open_world", "procedural_generation",
    "fighting_game", "combo_system", "frame_data", "hitbox_analysis", "character_balance",
    "racing_game", "vehicle_handling", "track_design", "physics_tire", "damage_model",
    "sports_game", "player_rating", "team_chemistry", "season_mode", "career_mode",
    "simulation_game", "economy_simulation", "city_building", "resource_management", "population_dynamics",
    "strategy_game", "tech_tree", "unit_balance", "map_control", "resource_gathering",
    "horror_game", "tension_building", "jump_scare", "atmosphere_design", "psychological_horror",
    "comedy_game", "humor_writing", "comedic_timing", "absurdist_humor", "satirical_element",
    "educational_game", "edutainment", "serious_game", "gamification", "learning_analytics",
    "esports_tournament", "competitive_balance", "spectator_mode", "replay_system", "matchmaking_algorithm",
    "mmo_system", "guild_management", "raid_design", "player_economy", "pvp_balancing",
    "game_marketing", "community_management", "live_operations", "battle_pass", "seasonal_content",
    "game_localization", "cultural_adaptation", "translation_pipeline", "regional_pricing", "certification_process",
]

random.shuffle(TOPICS27)
random.shuffle(TOPICS28)

ENTRIES = 1500
PREFIXES = ["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
SUFFIXES = ["A","B","C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]
LEVELS = ["Low","Medium","High","Critical","Optimal","Suboptimal","Degraded","Failing","Excellent","Good","Fair","Poor"]
STATUSES = ["Active","Inactive","Pending","Review","Approved","Rejected","Standby","Fault","Online","Offline","Maintenance","Commissioning"]

def generate_bulk(filename, topics, entries=ENTRIES):
    func_count = 0
    with open(filename, "w", encoding="utf-8") as f:
        f.write('"""{}: {} data functions, {} entries each."""\n'.format(os.path.basename(filename), len(topics), entries))
        f.write("import random\n\n")
        for spec in topics:
            frng = random.Random(hash(spec + "v5.3.0") % (2**31))
            func_name = spec
            func_count += 1
            f.write("\ndef get_{}_data():\n".format(func_name))
            f.write('    """Return {} entries of {} data."""\n'.format(entries, func_name.replace("_", " ")))
            f.write("    return [\n")
            for i in range(entries):
                name = "{}_{}_{}".format(
                    frng.choice(PREFIXES), frng.randint(100, 9999), frng.choice(SUFFIXES))
                val1 = round(frng.uniform(0.01, 9999.99), 2)
                val2 = frng.randint(1, 10000)
                val3 = frng.choice(LEVELS)
                val4 = round(frng.uniform(0.0, 100.0), 1)
                val5 = frng.choice(STATUSES)
                f.write('        ("{}", {}, {}, "{}", {}, "{}")'.format(name, val1, val2, val3, val4, val5))
                f.write(",\n" if i < entries - 1 else ",\n")
            f.write("    ]\n")
    total = os.path.getsize(filename)
    lines = (entries + 3) * func_count
    print("{}: {} functions, ~{} lines, {:.1f} KB".format(filename, func_count, lines, total/1024))

generate_bulk("data_bulk27.py", TOPICS27)
generate_bulk("data_bulk28.py", TOPICS28)
