# FHR Plank Multiphysics
power = 8741
htc =  611 
group_constants = "./fhr_assem_gc.json"

[GlobalParams]
  num_groups = 4
  num_precursor_groups = 6
  use_exp_form = false
  group_fluxes = 'group1 group2 group3 group4'
  pre_concs = 'pre1 pre2 pre3 pre4 pre5 pre6'
  temperature = 948 # K
  sss2_input = true
  account_delayed = true
  integrate_p_by_parts = true
[../]

[Mesh]
  file = '../fhr_assem.msh'
[]

[Problem]
  type = FEProblem
[]

[Variables]
  [./temp]
    family = LAGRANGE
    order = FIRST
    initial_condition = 923 # K
    scaling = 1e-8
  [../]
[]

[Nt]
  var_name_base = group
  create_temperature_var = false
  eigen = true
  scaling = 1
  pre_blocks = 'fuel_cell_0 fuel_cell_1 fuel_cell_2 fuel_cell_3 fuel_cell_4 fuel_cell_5 fuel_cell_6 fuel_cell_7 fuel_cell_8 fuel_cell_9 fuel_cell_10 fuel_cell_11 fuel_cell_12 fuel_cell_13 fuel_cell_14 fuel_cell_15 fuel_cell_16 fuel_cell_17 fuel_cell_18 fuel_cell_19 fuel_cell_20 fuel_cell_21 fuel_cell_22 fuel_cell_23 fuel_cell_24 fuel_cell_25 fuel_cell_26 fuel_cell_27 fuel_cell_28 fuel_cell_29 fuel_cell_30 fuel_cell_31 fuel_cell_32 fuel_cell_33 fuel_cell_34 fuel_cell_35 fuel_cell_36 fuel_cell_37 fuel_cell_38 fuel_cell_39 fuel_cell_40 fuel_cell_41 fuel_cell_42 fuel_cell_43 fuel_cell_44 fuel_cell_45 fuel_cell_46 fuel_cell_47 fuel_cell_48 fuel_cell_49 fuel_cell_50 fuel_cell_51 fuel_cell_52 fuel_cell_53 fuel_cell_54 fuel_cell_55 fuel_cell_56 fuel_cell_57 fuel_cell_58 fuel_cell_59'
[]

[Precursors]
  [./pres]
    var_name_base = pre
    outlet_boundaries = ''
    constant_velocity_values = true
    u_def = 0
    v_def = 0
    w_def = 0
    nt_exp_form = false
    family = MONOMIAL
    order = CONSTANT
    loop_precursors = false
    transient = false
    eigen = true
    scaling = 1e3
    block = 'fuel_cell_0 fuel_cell_1 fuel_cell_2 fuel_cell_3 fuel_cell_4 fuel_cell_5 fuel_cell_6 fuel_cell_7 fuel_cell_8 fuel_cell_9 fuel_cell_10 fuel_cell_11 fuel_cell_12 fuel_cell_13 fuel_cell_14 fuel_cell_15 fuel_cell_16 fuel_cell_17 fuel_cell_18 fuel_cell_19 fuel_cell_20 fuel_cell_21 fuel_cell_22 fuel_cell_23 fuel_cell_24 fuel_cell_25 fuel_cell_26 fuel_cell_27 fuel_cell_28 fuel_cell_29 fuel_cell_30 fuel_cell_31 fuel_cell_32 fuel_cell_33 fuel_cell_34 fuel_cell_35 fuel_cell_36 fuel_cell_37 fuel_cell_38 fuel_cell_39 fuel_cell_40 fuel_cell_41 fuel_cell_42 fuel_cell_43 fuel_cell_44 fuel_cell_45 fuel_cell_46 fuel_cell_47 fuel_cell_48 fuel_cell_49 fuel_cell_50 fuel_cell_51 fuel_cell_52 fuel_cell_53 fuel_cell_54 fuel_cell_55 fuel_cell_56 fuel_cell_57 fuel_cell_58 fuel_cell_59'
  [../]
[]

[Kernels]
  [./temp_conduction]
    type = ADHeatConduction
    variable = temp
    thermal_conductivity = 'k' 
  [../]
  [./heat_sink]
    type = ConvectiveHeatExchanger
    variable = temp
    htc = ${htc}
    tref = 923
    block = 'inner_flibe'
  [../]
  [./heat_source]
    type = FissionHeatSource
    variable = temp
    tot_fission_heat = powernorm
    power = ${power} # W
    block = 'fuel_cell_0 fuel_cell_1 fuel_cell_2 fuel_cell_3 fuel_cell_4 fuel_cell_5 fuel_cell_6 fuel_cell_7 fuel_cell_8 fuel_cell_9 fuel_cell_10 fuel_cell_11 fuel_cell_12 fuel_cell_13 fuel_cell_14 fuel_cell_15 fuel_cell_16 fuel_cell_17 fuel_cell_18 fuel_cell_19 fuel_cell_20 fuel_cell_21 fuel_cell_22 fuel_cell_23 fuel_cell_24 fuel_cell_25 fuel_cell_26 fuel_cell_27 fuel_cell_28 fuel_cell_29 fuel_cell_30 fuel_cell_31 fuel_cell_32 fuel_cell_33 fuel_cell_34 fuel_cell_35 fuel_cell_36 fuel_cell_37 fuel_cell_38 fuel_cell_39 fuel_cell_40 fuel_cell_41 fuel_cell_42 fuel_cell_43 fuel_cell_44 fuel_cell_45 fuel_cell_46 fuel_cell_47 fuel_cell_48 fuel_cell_49 fuel_cell_50 fuel_cell_51 fuel_cell_52 fuel_cell_53 fuel_cell_54 fuel_cell_55 fuel_cell_56 fuel_cell_57 fuel_cell_58 fuel_cell_59'
  [../]
[]

[Materials]
  [./ad_fuel]
    type = ADGenericConstantMaterial
    prop_names = 'k'
    prop_values = '0.099' # [W/(cm*K)] 
    block = 'fuel_cell_0 fuel_cell_1 fuel_cell_2 fuel_cell_3 fuel_cell_4 fuel_cell_5 fuel_cell_6 fuel_cell_7 fuel_cell_8 fuel_cell_9 fuel_cell_10 fuel_cell_11 fuel_cell_12 fuel_cell_13 fuel_cell_14 fuel_cell_15 fuel_cell_16 fuel_cell_17 fuel_cell_18 fuel_cell_19 fuel_cell_20 fuel_cell_21 fuel_cell_22 fuel_cell_23 fuel_cell_24 fuel_cell_25 fuel_cell_26 fuel_cell_27 fuel_cell_28 fuel_cell_29 fuel_cell_30 fuel_cell_31 fuel_cell_32 fuel_cell_33 fuel_cell_34 fuel_cell_35 fuel_cell_36 fuel_cell_37 fuel_cell_38 fuel_cell_39 fuel_cell_40 fuel_cell_41 fuel_cell_42 fuel_cell_43 fuel_cell_44 fuel_cell_45 fuel_cell_46 fuel_cell_47 fuel_cell_48 fuel_cell_49 fuel_cell_50 fuel_cell_51 fuel_cell_52 fuel_cell_53 fuel_cell_54 fuel_cell_55 fuel_cell_56 fuel_cell_57 fuel_cell_58 fuel_cell_59'
  [../]
  [./ad_graphite]
    type = ADGenericConstantMaterial
    prop_names = 'k'
    prop_values = '0.15' # [W/(cm*K)] 
    block = 'graphite_structure graphite_plank_1 graphite_plank_2 graphite_plank_3 graphite_plank_4 graphite_plank_5 graphite_plank_6'
  [../]
  [./ad_flibe]
    type = ADGenericConstantMaterial
    prop_names = 'k'
    prop_values = '0.01' # [W/(cm*K)] 
    block = 'outer_flibe inner_flibe slot_flibe'
  [../]
  [./fuel_cell_0]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_0'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_0'
  [../]
    [./fuel_cell_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_1'
  [../]
    [./fuel_cell_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_2'
  [../]
    [./fuel_cell_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_3'
  [../]
    [./fuel_cell_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_4'
  [../]
    [./fuel_cell_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_5'
  [../]
    [./fuel_cell_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_6'
  [../]
    [./fuel_cell_7]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_7'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_7'
  [../]
    [./fuel_cell_8]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_8'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_8'
  [../]
    [./fuel_cell_9]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_9'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_9'
  [../]
    [./fuel_cell_10]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_10'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_10'
  [../]
    [./fuel_cell_11]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_11'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_11'
  [../]
    [./fuel_cell_12]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_12'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_12'
  [../]
    [./fuel_cell_13]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_13'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_13'
  [../]
    [./fuel_cell_14]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_14'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_14'
  [../]
    [./fuel_cell_15]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_15'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_15'
  [../]
    [./fuel_cell_16]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_16'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_16'
  [../]
    [./fuel_cell_17]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_17'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_17'
  [../]
    [./fuel_cell_18]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_18'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_18'
  [../]
    [./fuel_cell_19]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_19'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_19'
  [../]
    [./fuel_cell_20]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_20'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_20'
  [../]
    [./fuel_cell_21]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_21'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_21'
  [../]
    [./fuel_cell_22]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_22'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_22'
  [../]
    [./fuel_cell_23]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_23'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_23'
  [../]
    [./fuel_cell_24]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_24'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_24'
  [../]
    [./fuel_cell_25]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_25'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_25'
  [../]
    [./fuel_cell_26]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_26'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_26'
  [../]
    [./fuel_cell_27]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_27'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_27'
  [../]
    [./fuel_cell_28]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_28'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_28'
  [../]
    [./fuel_cell_29]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_29'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_29'
  [../]
    [./fuel_cell_30]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_30'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_30'
  [../]
    [./fuel_cell_31]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_31'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_31'
  [../]
    [./fuel_cell_32]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_32'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_32'
  [../]
    [./fuel_cell_33]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_33'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_33'
  [../]
    [./fuel_cell_34]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_34'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_34'
  [../]
    [./fuel_cell_35]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_35'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_35'
  [../]
    [./fuel_cell_36]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_36'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_36'
  [../]
    [./fuel_cell_37]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_37'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_37'
  [../]
    [./fuel_cell_38]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_38'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_38'
  [../]
    [./fuel_cell_39]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_39'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_39'
  [../]
    [./fuel_cell_40]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_40'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_40'
  [../]
    [./fuel_cell_41]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_41'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_41'
  [../]
    [./fuel_cell_42]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_42'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_42'
  [../]
    [./fuel_cell_43]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_43'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_43'
  [../]
    [./fuel_cell_44]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_44'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_44'
  [../]
    [./fuel_cell_45]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_45'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_45'
  [../]
    [./fuel_cell_46]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_46'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_46'
  [../]
    [./fuel_cell_47]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_47'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_47'
  [../]
    [./fuel_cell_48]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_48'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_48'
  [../]
    [./fuel_cell_49]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_49'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_49'
  [../]
    [./fuel_cell_50]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_50'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_50'
  [../]
    [./fuel_cell_51]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_51'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_51'
  [../]
    [./fuel_cell_52]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_52'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_52'
  [../]
    [./fuel_cell_53]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_53'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_53'
  [../]
    [./fuel_cell_54]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_54'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_54'
  [../]
    [./fuel_cell_55]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_55'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_55'
  [../]
    [./fuel_cell_56]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_56'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_56'
  [../]
    [./fuel_cell_57]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_57'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_57'
  [../]
    [./fuel_cell_58]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_58'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_58'
  [../]
    [./fuel_cell_59]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_cell_59'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_cell_59'
  [../]
  [./graphite_structure]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_structure'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_structure'
  [../]
  [./graphite_plank_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_1'
  [../]
  [./graphite_plank_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_2'
  [../]
  [./graphite_plank_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_3'
  [../]
  [./graphite_plank_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_4'
  [../]
  [./graphite_plank_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_5'
  [../]
  [./graphite_plank_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_6'
  [../]
  [./outer_flibe]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'outer_flibe'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'outer_flibe'
  [../]
  [./inner_flibe]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'inner_flibe'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'inner_flibe'
  [../]
  [./slot_flibe]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'slot_flibe'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'slot_flibe'
  [../]
[]

[Executioner]
  type = NonlinearEigen
  max_power_iterations = 50

  #automatic_scaling = true
  #resid_vs_jac_scaling_param = 0.2
  #scaling_group_variables = 'group1 group2 group3 group4; pre1 pre2 pre3 pre4 pre5 pre6; temp'
  #compute_scaling_once = false

  # fission power normalization
  normalization = 'powernorm'
  normal_factor = ${power}  # W        

  xdiff = 'group1diff'
  bx_norm = 'bnorm'
  k0 = 1.40
  pfactor = 1e-2
  l_max_its = 1000
  nl_max_its = 5000
  nl_abs_tol = 1e-6

  free_power_iterations = 8

  solve_type = 'NEWTON'
  #petsc_options = '-snes_converged_reason -ksp_converged_reason -snes_linesearch_monitor'
  petsc_options_iname = '-pc_type -pc_factor_shift_type -pc_factor_mat_solver_package'
  petsc_options_value = 'lu       NONZERO               superlu_dist'
  #petsc_options_iname = '-pc_type -sub_pc_type -sub_pc_factor_shift_type'
  #petsc_options_value = 'asm      lu nonzero'
  line_search = none
[]

[Preconditioning]
  [./SMP]
    type = SMP
    full = true
  [../]
[]

[Postprocessors]
  [./bnorm]
    type = ElmIntegTotFissNtsPostprocessor
    execute_on = linear
  [../]
  [./tot_fissions]
    type = ElmIntegTotFissPostprocessor
    execute_on = linear
  [../]
  [./powernorm]
    type = ElmIntegTotFissHeatPostprocessor
    execute_on = linear
  [../]
  [./group1diff]
    type = ElementL2Diff
    variable = group1
    execute_on = 'linear timestep_end'
    use_displaced_mesh = false
  [../]
  [./group1_flux]
    type = ElementAverageValue
    variable = group1
    outputs = 'exodus console csv'
  [../]
  [./group2_flux]
    type = ElementAverageValue
    variable = group2
    outputs = 'exodus console csv'
  [../]
  [./group3_flux]
    type = ElementAverageValue
    variable = group3
    outputs = 'exodus console csv'
  [../]
  [./group4_flux]
    type = ElementAverageValue
    variable = group4
    outputs = 'exodus console csv'
  [../]
  [./temp_ave]
    type = ElementAverageValue
    variable = temp
    outputs = 'exodus console csv'
  [../]
  [./temp_max]
    type = NodalMaxValue
    variable = temp
    outputs = 'exodus console csv'
  [../]
[]

[VectorPostprocessors]
  [./flux_centerline]
   type = LineValueSampler
    variable = 'group1 group2 group3 group4 temp'
    start_point = '20.26 0 0'
    end_point = '20.26 23.4 0'
    num_points = 200
    sort_by = x
    execute_on = FINAL
  [../]
[]
[Outputs]
  perf_graph = true
  print_linear_residuals = true
  [./exodus]
    type = Exodus
  [../]
  [./csv]
    type = CSV
  [../]
[]

[Debug]
  show_var_residual_norms = true
[]