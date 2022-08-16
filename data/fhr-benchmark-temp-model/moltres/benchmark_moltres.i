# FHR Plank Multiphysics
power = 26223
htc =  611 
group_constants = "./benchmark_gc.json"

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
  file = './fhr_assem.msh'
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
  pre_blocks = 'fuel_stripe_1_1  fuel_stripe_1_2  fuel_stripe_1_3  fuel_stripe_1_4  fuel_stripe_1_5  fuel_stripe_1_6  fuel_stripe_1_7  fuel_stripe_1_8  fuel_stripe_1_9  fuel_stripe_1_10  fuel_stripe_1_11  fuel_stripe_1_12  fuel_stripe_2_1  fuel_stripe_2_2  fuel_stripe_2_3  fuel_stripe_2_4  fuel_stripe_2_5  fuel_stripe_2_6  fuel_stripe_2_7  fuel_stripe_2_8  fuel_stripe_2_9  fuel_stripe_2_10  fuel_stripe_2_11  fuel_stripe_2_12  fuel_stripe_3_1  fuel_stripe_3_2  fuel_stripe_3_3  fuel_stripe_3_4  fuel_stripe_3_5  fuel_stripe_3_6  fuel_stripe_3_7  fuel_stripe_3_8  fuel_stripe_3_9  fuel_stripe_3_10  fuel_stripe_3_11  fuel_stripe_3_12'
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
    block = 'fuel_stripe_1_1  fuel_stripe_1_2  fuel_stripe_1_3  fuel_stripe_1_4  fuel_stripe_1_5  fuel_stripe_1_6  fuel_stripe_1_7  fuel_stripe_1_8  fuel_stripe_1_9  fuel_stripe_1_10  fuel_stripe_1_11  fuel_stripe_1_12  fuel_stripe_2_1  fuel_stripe_2_2  fuel_stripe_2_3  fuel_stripe_2_4  fuel_stripe_2_5  fuel_stripe_2_6  fuel_stripe_2_7  fuel_stripe_2_8  fuel_stripe_2_9  fuel_stripe_2_10  fuel_stripe_2_11  fuel_stripe_2_12  fuel_stripe_3_1  fuel_stripe_3_2  fuel_stripe_3_3  fuel_stripe_3_4  fuel_stripe_3_5  fuel_stripe_3_6  fuel_stripe_3_7  fuel_stripe_3_8  fuel_stripe_3_9  fuel_stripe_3_10  fuel_stripe_3_11  fuel_stripe_3_12'
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
    block = 'outer_flibe slot_flibe inner_flibe_1 inner_flibe_2 inner_flibe_3'
  [../]
  [./heat_source]
    type = FissionHeatSource
    variable = temp
    tot_fission_heat = powernorm
    power = ${power} # W
    block = 'fuel_stripe_1_1  fuel_stripe_1_2  fuel_stripe_1_3  fuel_stripe_1_4  fuel_stripe_1_5  fuel_stripe_1_6  fuel_stripe_1_7  fuel_stripe_1_8  fuel_stripe_1_9  fuel_stripe_1_10  fuel_stripe_1_11  fuel_stripe_1_12  fuel_stripe_2_1  fuel_stripe_2_2  fuel_stripe_2_3  fuel_stripe_2_4  fuel_stripe_2_5  fuel_stripe_2_6  fuel_stripe_2_7  fuel_stripe_2_8  fuel_stripe_2_9  fuel_stripe_2_10  fuel_stripe_2_11  fuel_stripe_2_12  fuel_stripe_3_1  fuel_stripe_3_2  fuel_stripe_3_3  fuel_stripe_3_4  fuel_stripe_3_5  fuel_stripe_3_6  fuel_stripe_3_7  fuel_stripe_3_8  fuel_stripe_3_9  fuel_stripe_3_10  fuel_stripe_3_11  fuel_stripe_3_12'
  [../]
[]

[Materials]
  [./ad_fuel]
    type = ADGenericConstantMaterial
    prop_names = 'k'
    prop_values = '0.099' # [W/(cm*K)] 
    block = 'fuel_stripe_1_1  fuel_stripe_1_2  fuel_stripe_1_3  fuel_stripe_1_4  fuel_stripe_1_5  fuel_stripe_1_6  fuel_stripe_1_7  fuel_stripe_1_8  fuel_stripe_1_9  fuel_stripe_1_10  fuel_stripe_1_11  fuel_stripe_1_12  fuel_stripe_2_1  fuel_stripe_2_2  fuel_stripe_2_3  fuel_stripe_2_4  fuel_stripe_2_5  fuel_stripe_2_6  fuel_stripe_2_7  fuel_stripe_2_8  fuel_stripe_2_9  fuel_stripe_2_10  fuel_stripe_2_11  fuel_stripe_2_12  fuel_stripe_3_1  fuel_stripe_3_2  fuel_stripe_3_3  fuel_stripe_3_4  fuel_stripe_3_5  fuel_stripe_3_6  fuel_stripe_3_7  fuel_stripe_3_8  fuel_stripe_3_9  fuel_stripe_3_10  fuel_stripe_3_11  fuel_stripe_3_12'
  [../]
  [./ad_graphite]
    type = ADGenericConstantMaterial
    prop_names = 'k'
    prop_values = '0.15' # [W/(cm*K)] 
    block = 'graphite_structure spacers graphite_plank_1_1  graphite_plank_1_2  graphite_plank_1_3  graphite_plank_1_4  graphite_plank_1_5  graphite_plank_1_6  graphite_plank_2_1  graphite_plank_2_2  graphite_plank_2_3  graphite_plank_2_4  graphite_plank_2_5  graphite_plank_2_6  graphite_plank_3_1  graphite_plank_3_2  graphite_plank_3_3  graphite_plank_3_4  graphite_plank_3_5  graphite_plank_3_6'
  [../]
  [./ad_flibe]
    type = ADGenericConstantMaterial
    prop_names = 'k'
    prop_values = '0.01' # [W/(cm*K)] 
    block = 'outer_flibe slot_flibe inner_flibe_1 inner_flibe_2 inner_flibe_3'
  [../]
  [./fuel_stripe_1_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_1'
  [../]
    [./fuel_stripe_1_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_2'
  [../]
    [./fuel_stripe_1_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_3'
  [../]
    [./fuel_stripe_1_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_4'
  [../]
    [./fuel_stripe_1_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_5'
  [../]
    [./fuel_stripe_1_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_6'
  [../]
    [./fuel_stripe_1_7]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_7'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_7'
  [../]
    [./fuel_stripe_1_8]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_8'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_8'
  [../]
    [./fuel_stripe_1_9]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_9'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_9'
  [../]
    [./fuel_stripe_1_10]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_10'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_10'
  [../]
    [./fuel_stripe_1_11]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_11'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_11'
  [../]
    [./fuel_stripe_1_12]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_1_12'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_1_12'
  [../]
    [./fuel_stripe_2_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_1'
  [../]
    [./fuel_stripe_2_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_2'
  [../]
    [./fuel_stripe_2_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_3'
  [../]
    [./fuel_stripe_2_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_4'
  [../]
    [./fuel_stripe_2_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_5'
  [../]
    [./fuel_stripe_2_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_6'
  [../]
    [./fuel_stripe_2_7]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_7'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_7'
  [../]
    [./fuel_stripe_2_8]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_8'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_8'
  [../]
    [./fuel_stripe_2_9]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_9'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_9'
  [../]
    [./fuel_stripe_2_10]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_10'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_10'
  [../]
    [./fuel_stripe_2_11]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_11'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_11'
  [../]
    [./fuel_stripe_2_12]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_2_12'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_2_12'
  [../]
    [./fuel_stripe_3_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_1'
  [../]
    [./fuel_stripe_3_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_2'
  [../]
    [./fuel_stripe_3_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_3'
  [../]
    [./fuel_stripe_3_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_4'
  [../]
    [./fuel_stripe_3_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_5'
  [../]
    [./fuel_stripe_3_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_6'
  [../]
    [./fuel_stripe_3_7]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_7'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_7'
  [../]
    [./fuel_stripe_3_8]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_8'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_8'
  [../]
    [./fuel_stripe_3_9]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_9'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_9'
  [../]
    [./fuel_stripe_3_10]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_10'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_10'
  [../]
    [./fuel_stripe_3_11]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_11'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_11'
  [../]
    [./fuel_stripe_3_12]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'fuel_stripe_3_12'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel_stripe_3_12'
  [../]
  [./spacers]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'spacers'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'spacers'
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
  [./graphite_plank_1_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_1_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_1_1'
  [../]
    [./graphite_plank_1_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_1_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_1_2'
  [../]
    [./graphite_plank_1_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_1_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_1_3'
  [../]
    [./graphite_plank_1_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_1_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_1_4'
  [../]
    [./graphite_plank_1_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_1_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_1_5'
  [../]
    [./graphite_plank_1_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_1_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_1_6'
  [../]
    [./graphite_plank_2_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_2_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_2_1'
  [../]
    [./graphite_plank_2_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_2_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_2_2'
  [../]
    [./graphite_plank_2_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_2_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_2_3'
  [../]
    [./graphite_plank_2_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_2_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_2_4'
  [../]
    [./graphite_plank_2_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_2_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_2_5'
  [../]
    [./graphite_plank_2_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_2_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_2_6'
  [../]
    [./graphite_plank_3_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_3_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_3_1'
  [../]
    [./graphite_plank_3_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_3_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_3_2'
  [../]
    [./graphite_plank_3_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_3_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_3_3'
  [../]
    [./graphite_plank_3_4]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_3_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_3_4'
  [../]
    [./graphite_plank_3_5]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_3_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_3_5'
  [../]
    [./graphite_plank_3_6]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'graphite_plank_3_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite_plank_3_6'
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
  [./inner_flibe_1]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'inner_flibe_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'inner_flibe_1'
  [../]
  [./inner_flibe_2]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'inner_flibe_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'inner_flibe_2'
  [../]
  [./inner_flibe_3]
    type = MoltresJsonMaterial
    base_file = ${group_constants}
    material_key = 'inner_flibe_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'inner_flibe_3'
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
    start_point = '0 -23.4 0'
    end_point = '0 +23.4 0'
    num_points = 1000
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