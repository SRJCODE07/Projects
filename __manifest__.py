{
    'name': "College Management",
    'version': '17.0.0.1',
    'depends': ['base'],
    'author': "Shubham Saroj",
    'category': 'Category',
    'description': """
    College Management system
    """,
    # data files always loaded at installation
    'data': [
        # Security
        "security/ir.model.access.csv",
        
        # Views
        "views/college_student_views.xml",
        "views/student_hobbies_views.xml",
        "views/student_course_views.xml",
        "views/college_staff_views.xml",
        "views/college_department_views.xml",
        "views/college_fees_views.xml",
        "views/college_subject_views.xml",
        "views/menu_views.xml"



    ],
    # data files containing optionally loaded demonstration data
    'license': "LGPL-3"
}