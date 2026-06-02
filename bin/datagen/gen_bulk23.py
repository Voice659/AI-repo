"""Generate data_bulk23.py: 200 robotics & automation data functions, 200K+ lines."""
import random, os

random.seed(2323)

TOPICS = [
    "industrial_robot", "collaborative_robot", "autonomous_drone", "self_driving_car",
    "warehouse_automation", "assembly_line_robot", "welding_robot", "painting_robot",
    "packaging_robot", "palletizing_robot", "inspection_robot", "sorting_robot",
    "pick_and_place", "cnc_machine", "3d_printer_industrial", "laser_cutter",
    "waterjet_cutter", "plasma_cutter", "conveyor_system", "automated_guided_vehicle",
    "autonomous_mobile_robot", "humanoid_robot", "exoskeleton", "prosthetic_limb",
    "robot_arm_6dof", "robot_arm_7dof", "gripper_mechanism", "suction_gripper",
    "magnetic_gripper", "soft_robot", "swarm_robot", "underwater_robot",
    "space_robot", "surgical_robot", "rehabilitation_robot", "telepresence_robot",
    "social_robot", "educational_robot", "toy_robot", "companion_robot",
    "security_robot", "cleaning_robot", "lawn_mowing_robot", "agricultural_robot",
    "milking_robot", "greenhouse_automation", "food_processing_robot", "beverage_bottling",
    "pharma_automation", "lab_automation", "microscope_automation", "sensor_network",
    "iot_device", "smart_home_device", "smart_lock", "smart_thermostat",
    "smart_lighting", "smart_speaker", "smart_display", "smart_appliance",
    "connected_sensor", "temperature_sensor", "pressure_sensor", "proximity_sensor",
    "motion_sensor", "gas_sensor", "humidity_sensor", "light_sensor",
    "accelerometer", "gyroscope", "magnetometer", "force_sensor",
    "torque_sensor", "encoder_optical", "lidar_sensor", "radar_sensor",
    "ultrasonic_sensor", "camera_module", "depth_camera", "thermal_camera",
    "spectrometer", "barcode_scanner", "rfid_reader", "nfc_reader",
    "control_system_plc", "control_system_scada", "control_system_dcs", "cnc_controller",
    "motor_driver", "stepper_motor", "servo_motor", "brushless_motor",
    "linear_actuator", "pneumatic_actuator", "hydraulic_actuator", "piezoelectric_actuator",
    "power_supply", "battery_system", "solar_panel", "fuel_cell",
    "supercapacitor", "wireless_charger", "energy_harvester", "gearbox_type",
    "bearing_type", "belt_drive", "chain_drive", "ball_screw",
    "linear_guide", "vacuum_pump", "air_compressor", "hydraulic_pump",
    "heat_exchanger", "cooling_system", "vision_system", "machine_vision",
    "object_detection", "facial_recognition", "gesture_recognition", "speech_recognition",
    "nlp_engine", "recommendation_system", "predictive_maintenance", "digital_twin",
    "simulation_software", "robot_os", "robot_middleware", "path_planning",
    "motion_planning", "inverse_kinematics", "forward_kinematics", "trajectory_planning",
    "obstacle_avoidance", "slam_algorithm", "localization_system", "mapping_algorithm",
    "navigation_system", "fleet_management", "task_scheduler", "resource_allocator",
    "collision_detection", "safety_light_curtain", "safety_mat", "emergency_stop",
    "interlock_system", "protective_fence", "sensor_fusion", "filter_kalman",
    "filter_particle", "pid_controller", "adaptive_control", "fuzzy_logic",
    "neural_network_control", "reinforcement_learning", "supervised_learning_robot", "unsupervised_learning_robot",
    "calibration_system", "diagnostic_system", "remote_monitoring", "cloud_robotics",
    "edge_computing", "fog_computing", "digital_output_module", "digital_input_module",
    "analog_module", "communication_protocol", "ethernet_ip", "profinet",
    "modbus_tcp", "can_bus", "device_net", "io_link",
    "opc_ua", "mqtt_broker", "robot_language", "programming_pendant",
    "teach_pendant", "offline_programming", "robot_calibration", "tool_center_point",
    "singularity_handling", "force_control", "impedance_control", "admittance_control",
    "compliant_motion", "seam_tracking", "arc_welding", "spot_welding",
    "laser_welding", "ultrasonic_welding", "adhesive_dispensing", "screw_driving",
    "riveting_robot", "deburring_robot", "polishing_robot", "grinding_robot",
    "waterjet_cutting_robot", "laser_cutting_robot", "plasma_cutting_robot", "drilling_robot",
    "routing_robot", "painting_booth_robot", "coating_robot", "dip_molding",
    "injection_molding_robot", "die_casting_robot", "forging_robot", "stamping_press",
    "bending_machine", "tube_bending_robot", "wire_harness_robot", "cable_management",
    "pcb_assembly", "solder_robot", "through_hole_solder", "reflow_soldering",
    "wave_soldering", "selective_solder", "potting_robot", "encapsulation_robot",
    "labeling_machine", "marking_machine", "engraving_robot", "testing_probe",
    "quality_inspection", "vision_inspection", "xray_inspection", "leak_testing",
    "torque_testing", "tensile_testing", "hardness_testing", "dimensional_inspection",
    "coordinate_measuring", "surface_roughness", "cleanroom_robot", "sterile_filling",
    "capping_machine", "cartoning_machine", "case_packer", "stretch_wrapper",
    "strapping_machine", "shrink_wrapper", "pallet_stacker", "pallet_stretcher",
    "depalletizer", "goods_to_person", "put_to_light", "voice_picking",
    "augmented_reality_pick", "cobot_safety", "power_limiting", "speed_monitoring",
    "separation_distance", "hand_guiding", "direct_teach", "lead_through",
]

random.shuffle(TOPICS)

COLUMNS = "Name,Type,Year,Manufacturer,Applications,Power_kW,Weight_kg,Accuracy_mm".split(",")
COLUMN_COUNT = len(COLUMNS)

ENTRIES = 1000
func_count = 0

with open("../datab/data_bulk23.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk23.py: 200 robotics & automation data functions, 1000 entries each, ~200K lines."""\n')
    f.write("import random\n\n")

    for spec in TOPICS:
        rng = random.Random(hash(spec + "v5.1.0.23") % (2**31))
        func_name = spec
        func_count += 1

        f.write("\ndef get_{}_data():\n".format(func_name))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            name = "{} {}-{}".format(
                random.choice(["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon"]),
                random.choice(["A","B","C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]),
                rng.randint(1000, 9999)
            )
            typ = random.choice(["Stationary","Mobile","Articulated","SCARA","Delta","Cartesian","Cylindrical","Spherical","Parallel","Collaborative","Dual-Arm","Single-Arm","Torso","Legged","Wheeled","Tracked","Aerial","Underwater","Wearable","Modular"])
            year = rng.randint(1990, 2026)
            manufacturer = random.choice(["Fanuc","ABB","Kuka","Yaskawa","Universal Robots","Staubli","Epson","Kawasaki","Mitsubishi","Denso","Nachi","Comau","Hyundai","Doosan","Omron","Adept","Motoman","Panasonic","Siemens","Bosch Rexroth"])
            apps = random.choice(["Assembly","Welding","Painting","Material Handling","Packaging","Palletizing","Machine Tending","Inspection","Dispensing","Cutting","Grinding","Polishing","Deburring","Screw Driving","Glueing","Soldering","Testing","Pick and Place","Sorting","Labeling"])
            power = round(rng.uniform(0.1, 50.0), 2)
            weight = rng.randint(5, 5000)
            accuracy = round(rng.uniform(0.01, 5.0), 3)

            f.write('        ("{}", "{}", {}, "{}", "{}", {}, {}, {})'.format(
                name, typ, year, manufacturer, apps, power, weight, accuracy
            ))
            f.write(",\n" if i < ENTRIES - 1 else ",\n")

        f.write("    ]\n")

total = os.path.getsize("data_bulk23.py") if os.path.exists("data_bulk23.py") else 0
lines_est = (ENTRIES + 3) * func_count
print("Generated data_bulk23.py: {} functions, ~{} lines, {:.1f} KB".format(func_count, lines_est, total/1024))
