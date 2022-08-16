[GlobalParams]
  num_groups = 4
  num_precursor_groups = 6
  use_exp_form = false
  group_fluxes = 'group1 group2 group3 group4'
  pre_concs = 'pre1 pre2 pre3 pre4 pre5 pre6'
  temperature = 948 # all material temperatures?
  sss2_input = true
  account_delayed = false
[../]

[Mesh]
  file = 'fhr_plank.msh'
[]

[Problem]
  type = FEProblem

[]

[Nt]
  var_name_base = group
  #vacuum_boundaries = 'out'
  create_temperature_var = false
  eigen = true
  transient = false
  scaling = 1e3
  pre_blocks = 'fuel1 fuel2 fuel3 fuel4 fuel5 fuel6 fuel7 fuel8 fuel9 fuel10'
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
    scaling = 1e3
    eigen = true
    block = 'fuel1 fuel2 fuel3 fuel4 fuel5 fuel6 fuel7 fuel8 fuel9 fuel10'
  [../]
[]

[Materials]
  [./fuel1]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel1'
  [../]
  [./fuel2]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel2'
  [../]
  [./fuel3]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_3'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel3'
  [../]
  [./fuel4]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_4'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel4'
  [../]
  [./fuel5]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_5'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel5'
  [../]
  [./fuel6]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_6'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel6'
  [../]
  [./fuel7]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_7'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel7'
  [../]
  [./fuel8]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_8'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel8'
  [../]
  [./fuel9]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_9'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel9'
  [../]
  [./fuel10]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'prism_cell_10'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'fuel10'
  [../]
  [./graphite1]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'graphite1'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite1'
  [../]
  [./graphite2]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'graphite2'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'graphite2'
  [../]
  [./flibe]
    type = MoltresJsonMaterial
    base_file = '../plank_10_slice_refl/140pcm-moltres-gc/fhr_plank.json'
    material_key = 'bounds'
    interp_type = 'linear'
    prop_names = ''
    prop_values = '' 
    block = 'flibe'
  [../]
[]

[Executioner]
  type = InversePowerMethod
  max_power_iterations = 50
  normalization = 'powernorm'
  normal_factor = 210353

  xdiff = 'group1diff'
  bx_norm = 'bnorm'
  k0 = 1.004
  l_max_its = 100
  eig_check_tol = 1e-7

   solve_type = 'NEWTON'
#  petsc_options = '-snes_converged_reason -ksp_converged_reason -snes_linesearch_monitor'
#  petsc_options_iname = '-pc_type -pc_factor_shift_type -pc_factor_mat_solver_package'
#  petsc_options_value = 'lu       NONZERO               superlu_dist'

## Use the settings below instead if running on a desktop/small cluster
   petsc_options_iname = '-pc_type -sub_pc_type -ksp_gmres_restart -pc_asm_overlap -sub_pc_factor_shift_type'
   petsc_options_value = 'asm      lu           200                1               NONZERO'

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
  [./group1norm]
    type = ElementIntegralVariablePostprocessor
    variable = group1
    execute_on = linear
  [../]
  [./group1max]
    type = NodalMaxValue
    variable = group1
    execute_on = timestep_end
  [../]
  [./group1diff]
    type = ElementL2Diff
    variable = group1
    execute_on = 'linear timestep_end'
    use_displaced_mesh = false
  [../]
  [./group2norm]
    type = ElementIntegralVariablePostprocessor
    variable = group2
    execute_on = linear
  [../]
  [./group2max]
    type = NodalMaxValue
    variable = group2
    execute_on = timestep_end
  [../]
  [./group2diff]
    type = ElementL2Diff
    variable = group2
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
[]

[VectorPostprocessors]
  [./flux_centerline]
   type = LineValueSampler
    variable = 'group1 group2 group3 group4'
    start_point = '0 1.625 0'
    end_point = '27.1 1.625 0'
    num_points = 100
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