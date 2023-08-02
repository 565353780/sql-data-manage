PERSON_TITLE_LIST = [
    'gender',
    'age',
    'birthday',
    'marriage',
    'occpation',
    'nationality',
    'height',
    'weight',
    'birth_weight',
]

PRIVATE_TITLE_LIST = [
    'order_id',
    'order_id_his',
    'patient_no',
    'patient_type',
    'name',
    'address',
    'id_card',
    'phone',
]

INSO_TITLE_LIST = [
    'insu_type_code',
    'insu_no',
    'reimb_no',
    'reimb_type',
    'reimb_type_code',
    'reimb_org',
    'bal_date',
    'bal_date_s',
    'deal_date',
    'unreimb_fee',
    'css',
    'cas',
    'self_amount_acc',
    'self_pay',
    'large_fee_s',
    'effect_fee_s',
    'reserve_fee_s',
    'reimb_thres',
    'basic_fee',
]

CHILD_TITLE_LIST = [
    'pregnancy',
    'time_of_preg',
    'breast_feeding',
    'neonate',
    'infant_bind',
]

MEDICAL_TITLE_LIST = [
    'clinical_path',
    'single_code',
    'single_code_name',
    'allergy_list',
    'in_date',
    'out_date',
    'in_dept',
    'in_dept_id',
    'out_dept',
    'out_dept_id',
    'enter_type',
    'enter_type_code',
    'leave_type',
    'leave_type_code',
    'rescue_times',
    'rescue_succ_times',
    'pathologic_name',
]

HOSPITAL_TITLE_LIST = [
    'total_fee',
    'bedday_fee',
    'amount_acc',
    'large_fee',
    'effect_fee',
    'region_id',
    'region_name',
]

ILL_TITLE_LIST = [
    'diagnose',
    'drg',
    'drg_name',
    'drg_one',
    'drg_two',
    'drg_flag',
    'danger',
    'order',
    'ss_name',
    'use_ventilator_day',
    'use_ventilator_hour',
    'use_ventilator_min',
    'nwb_age',
    'act_ipt_days',
    'diag_code_cnt',
    'oprn_oprt_code_cnt',
    'bld_amt',
    'spga_nurscare_days',
    'primary_nurscare_days',
    'scd_nurscare_days',
    'tertiary_nurscare_days',
    'dip_diag_code',
    'dip_diag_name',
    'dip_oper_code',
    'dip_oper_name',
    'dip_score',
]

DOCTOR_TITLE_LIST = [
    'doc_id',
    'doc_name',
    'doc_title',
    'doc_group',
    'pathologic_diag',
]

INFO_QUERY_TITLE_LIST = \
    PERSON_TITLE_LIST + \
    CHILD_TITLE_LIST + \
    MEDICAL_TITLE_LIST + \
    HOSPITAL_TITLE_LIST + \
    ILL_TITLE_LIST
