from django.urls import path
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.urls import include, re_path

# password reset
from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy

app_name = 'activities'

urlpatterns = [
    path('', views.index, name='index'),
    path('navbar/', views.navbar, name='navbar'),
    path('admin_nav/', views.admin_nav, name='admin_nav'),
    path('logout_student/', views.logout_student, name='logout_student'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('signup/', views.signup, name='signup'),
    path('login_page/',views.login_page, name='login_page'),
    path('signin/', views.signin, name='signin'),
    path('dashboard_page/', views.dashboard_page, name='dashboard_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('others/', views.others, name='others'),
    path('edit_others/<str:id>', views.edit_others, name='edit_others'),
    # path('health/', views.health, name='health'),
    path('edit_health/', views.edit_health, name='edit_health'),
    path('file_manager/', views.file_manager, name='file_manager'),
    path('files_rotc/', views.files_rotc, name='files_rotc'),
    path('rotc_files/', views.rotc_files, name='rotc_files'),
    path('files_cwts/', views.files_cwts, name='files_cwts'),
    path('cwts_files/', views.cwts_files, name='cwts_files'),
    path('fields/', views.fields, name='fields'),
    path('field_rotc/', views.field_rotc, name='field_rotc'),
    
    
    
    # admin urls
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_staff/', views.admin_staff, name='admin_staff'),
    path('admin_pending/', views.admin_pending, name='admin_pending'),
    path('admin_view_profile/<str:id>', views.admin_view_profile, name='admin_view_profile'),
    path('approve/<str:idnumber>', views.approve, name='approve'),
    path('decline/<str:id>', views.decline, name='decline'),
    path('admin_rejected/', views.admin_rejected, name='admin_rejected,'),
    path('custom/', views.custom, name='custom'),
    path('rejected_email_page/<str:id>', views.rejected_email_page, name='rejected_email_page'),
    path('school_years/', views.school_years, name='school_years'),
    path('create_sy/', views.create_sy, name='create_sy'),
    # path('allumni_page/', views.allumni_page, name='allumni_page'),
    path('allumni_content/', views.allumni_content, name='allumni_content'),
    path('delete_sy/<str:years>', views.delete_sy, name='delete_sy'),
    path('create_platoon_page/', views.create_platoon_page, name='create_platoon_page'),
    path('create_section/', views.create_section, name='create_section'),
    path('counts/', views.counts, name='counts'),
    path('pl_content/', views.pl_content, name='pl_content'),
    path('section_content/', views.section_content, name='section_content'),
    path('view_images/<str:id>', views.view_images, name='view_images'),
    path('create_platoon_page2/', views.create_platoon_page2, name='create_platoon_page2'),
    path('manage_section/', views.manage_section, name='manage_section'),
    path('edit_manage/<str:id>', views.edit_manage, name='edit_manage'),
    path('export/', views.export, name='export'),
    path('edit_student/<str:id>', views.edit_student, name='edit_student'),
    path('attendance_page/', views.attendance_page, name='attendance_page'),
    path('create_day/',views.create_day, name='create_day'),
    path('create_annoucement/', views.create_announcement, name='create_announcement'),
    path('edit_announcement/<str:id>', views.edit_announcement, name='edit_announcement'),
    path('delete_announcement/<str:id>', views.delete_announcement, name='delete_announcement'),
    path('attendance_sections/', views.attendance_sections, name='attendance_sections'),
    path('attendance_main/', views.attendance_main, name='attendance_main'),
    path('attendance_main_page/', views.attendance_main_page, name='attendance_main_page'),
    # path('record/<str:id>', views.record, name='record'),
    path('update_attendance/', views.update_attendance, name='update_attendance'),
    path('add_students/', views.add_students, name='add_students'),
    path('assign_section/', views.assign_section, name='assign_section'),
    path('update_sy/', views.update_sy, name='update_sy'),
    path('update_officially/<str:id>', views.update_officially, name='update_officially'),
    path('cert_page/', views.cert_page, name='cert_page'),
    path('generate/', views.generate, name='generate'),
    path('open_cert_page/', views.open_cert_page, name='open_cert_page'),
    path('add_details/', views.add_details, name='add_details'),
    path('update_acts/', views.update_acts, name='update_acts'),
    path('r_approve/<str:idnumber>', views.r_approve, name='r_approve'),
    path('r_decline/<str:idnumber>', views.r_decline, name='r_decline'),
    path('download/', views.download, name='download'),
    path('download1/', views.download1, name='download1'),
    path('update_manage/', views.update_manage, name='update_manage'),
    path('admin_files/', views.admin_files, name='admin_files'),
    path('open_folder/<str:section_created>', views.open_folder, name='open_folder'),
    path('dropped/', views.dropped, name='dropped'),
    path('download3/', views.download3, name='download3'),
  
    path('download4/', views.download4, name='download4'),
    path('sample_attendance/', views.sample_attendance, name='sample_attendance'),
    path('create_td/', views.create_td, name='create_td'),
    path('open_date/', views.open_date, name='open_date'),
    path('open_sections/', views.open_sections, name='open_sections'),
    path('all_sections/', views.all_sections, name='all_sections'),
    path('del_tday/<str:id>', views.del_tday, name='del_tday'),
    path('download5/', views.download5, name='download5'),
    path('rec_attendance/', views.rec_attendance, name='rec_attendance'),
    path('show_students/', views.show_students, name='show_students'),
    path('update_sys/', views.update_sys, name='update_sys'),
    path('update_att_credits/', views.update_att_credits, name='update_att_credits'),
    path('grades/', views.grades, name='grades'),
    path('modify_grades/', views.modify_grades, name='modify_grades'),
    path('set_activities/', views.set_activities, name='set_activities'),
    path('save_grade/', views.save_grade, name='save_grade'),
    path('edit_activities/<str:id>', views.edit_activities, name='edit_activities'),
    path('delete_activities/<str:id>', views.delete_activities, name='delete_activities'),
    path('attendance_tab/', views.attendance_tab, name='attendance_tab'),
    path('create_td2/', views.create_td2, name='create_td2'),
    path('delete_td/<str:id>', views.delete_td, name='delete_td'),
    path('midterms/', views.midterms, name='midterms'),
    path('add_midterm/', views.add_midterm, name='add_midterm'),
    path('modify_midterm/', views.modify_midterm, name='modify_midterm'),
    # path('save_grade_2/', views.save_grade_2, name='save_grade_2'),
    path('save_midterm/', views.save_midterm, name='save_midterm'),
    path('finals_/', views.finals_, name='finals_'),
    path('modify_finals/', views.modify_finals, name='modify_finals'),
    path('add_finals/', views.add_finals, name='add_finals'),
    path('delete_midterm/<str:id>', views.delete_midterm, name='delete_midterm'),
    path('delete_finals/<str:id>', views.delete_finals, name='delete_finals'),
    path('save_finals/', views.save_finals, name='save_finals'),
    path('final_grade/', views.final_grade, name='final_grade'),
    path('access_final_grade/', views.access_final_grade, name='access_final_grade'),
    path('save_finale_grades/', views.save_finale_grades, name='save_finale_grades'),
    path('merits/', views.merits, name='merits'),
    path('access_merits/', views.access_merits, name='access_merits'),
    path('save_merits/', views.save_merits, name='save_merits'),
    path('approve2/<str:id>', views.approve2, name='approve2'),
    path('decline2/<str:id>', views.decline2,name='decline2'),
    path('custom36/', views.custom36, name='custom36'),
    path('open_csv/', views.open_csv, name='open_csv'),
    path('open_wala/', views.open_wala, name='open_wala'),
    path('read_attendance/', views.read_attendance, name='read_attendance'),
    path('before_csv/', views.before_csv, name='before_csv'),
    path('update_section/', views.update_section, name='update_section'),
    path('cwts_attendance/', views.cwts_attendance, name='cwts_attendance'),
    path('cwts_td/', views.cwts_td, name='cwts_td'),
    path('open_cwts_date/', views.open_cwts_date, name='open_cwts_date'),
    path('display_csv/', views.display_csv, name='display_csv'),
    path('open_cwts_csv/', views.open_cwts_csv, name='open_cwts_csv'),
    path('save_cwts_attendance/', views.save_cwts_attendance, name='save_cwts_attendance'),
    path('del_cwts_tday/<str:id>', views.del_cwts_tday, name='del_cwts_tday'),
    path('cwts_attendance_tab/', views.cwts_attendance_tab, name='cwts_attendance_tab'),
    path('cwts_show_students/', views.cwts_show_students, name='cwts_show_students'),
    path('cwts_course_evaluation/', views.cwts_course_evaluation, name='cwts_course_evaluation'),
    path('save_evaluation/', views.save_evaluation, name='save_evaluation'),
    path('update_att_credits_cwts/', views.update_att_credits_cwts, name='update_att_credits_cwts'),
    path('quiz/', views.quiz, name='quiz'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('cwts_edit_activities/<str:id>', views.cwts_edit_activities, name='cwts_edit_activities'),
    path('cwts_delete_activities/<str:id>', views.cwts_delete_activities, name='cwts_delete_activities'),
    path('cwts_modify_grades/', views.cwts_modify_grades, name='cwts_modify_grades'),
    path('cwts_save_grade/', views.cwts_save_grade, name='cwts_save_grade'),
    path('exercises/', views.exercises, name='exercises'),
    path('cwts_access_exercises/', views.cwts_access_exercises, name='cwts_access_exercises'),
    path('add_exercises/', views.add_exercises, name='add_exercises'),
    path('cwts_save_exercises/', views.cwts_save_exercises, name='cwts_save_exercises'),
    path('cwts_midterms/', views.cwts_midterms, name='cwts_midterms'),
    path('cwts_add_midterm/', views.cwts_add_midterm, name='cwts_add_midterm'),
    path('delete_cwts_midterm/<str:id>', views.delete_cwts_midterm, name='delete_cwts_midterm'),
    path('modify_cwts_midterm/', views.modify_cwts_midterm, name='modify_cwts_midterm'),
    path('save_cwts_midterm/', views.save_cwts_midterm, name='save_cwts_midterm'),
    path('cwts_finals/', views.cwts_finals, name='cwts_finals'),
    path('modify_cwts_finals/', views.modify_cwts_finals, name='modify_cwts_finals'),
    path('add_cwts_finals/', views.add_cwts_finals, name='add_cwts_finals'),
    path('save_cwts_finals/', views.save_cwts_finals, name='save_cwts_finals'),
    path('delete_cwts_finals/<str:id>', views.delete_cwts_finals, name='delete_cwts_finals'),
    path('cwts_final_grade/', views.cwts_final_grade, name='cwts_final_grade'),
    path('access_cwts_final_grade/', views.access_cwts_final_grade, name='access_cwts_final_grade'),
    path('save_cwts_finale_grades/', views.save_cwts_finale_grades, name='save_cwts_finale_grades'),
    path('file_upload_index/', views.file_upload_index, name='file_upload_index'),
    path('health/', views.health, name='health'),
    path('each_student/<str:id>', views.each_student, name='each_student'),
    path('update_each_student/', views.update_each_student, name='update_each_student'),
    path('custom999/', views.custom999, name='custom999'),
    path('manage_cwts_section/', views.manage_cwts_section, name='manage_cwts_section'),
    path('cwts_section_content/', views.cwts_section_content, name='cwts_section_content'),
    path('cwts_each_student/<str:id>', views.cwts_each_student, name='cwts_each_student'),
    path('cwts_each_student_2/<str:id>', views.cwts_each_student_2, name='cwts_each_student_2'),
    path('add_cwts_students/', views.add_cwts_students, name='add_cwts_students'),
    path('assign_cwts_section/', views.assign_cwts_section, name='assign_cwts_section'),
    path('cwts_cert_page/', views.cwts_cert_page, name='cwts_cert_page'),
    path('cwts_add_details/', views.cwts_add_details, name='cwts_add_details'),
    path('cwts_generate/', views.cwts_generate, name='cwts_generate'),
    path('cwts_update_acts/', views.cwts_update_acts, name='cwts_update_acts'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('delete_files/<str:id>', views.delete_files, name='delete_files'),
    path('cwts_file_upload/', views.cwts_file_upload, name='cwts_file_upload'),
    path('cwts_upload_file/', views.cwts_upload_file, name='cwts_upload_file'),
    path('delete_cfiles/<str:id>', views.delete_cfiles, name='delete_cfiles'),
    path('rotc_alumni/', views.rotc_alumni, name='rotc_alumni'),
    path('alumni_years/', views.alumni_years, name='alumni_years'),
    path('each_alumni/<str:id>', views.each_alumni, name='each_alumni'),
    path('update_each_graduates/', views.update_each_graduates, name='update_each_graduates'),
    path('cwts_alumni/', views.cwts_alumni, name='cwts_alumni'),
    path('cwts_alumni_years/', views.cwts_alumni_years, name='cwts_alumni_years'),
    path('cwts_each_alumni/<str:id>', views.cwts_each_alumni, name='cwts_each_alumni'),
    path('update_each_cwts_graduates/', views.update_each_cwts_graduates, name='update_each_cwts_graduates'),
    path('add_alumni_years/', views.add_alumni_years, name='add_alumni_years'),
    path('alumni_year/<str:id>', views.alumni_year, name='alumni_year'),
    path('cwts_alumni_year/<str:id>', views.cwts_alumni_year, name='cwts_alumni_year'),
    path('send_feedback/', views.send_feedback, name='send_feedback'),
    path('send_response/', views.send_response, name='send_response'),
    path('student_update/', views.student_update, name='student_update'),
    path('all_files/', views.all_files, name='all_files'),
    path('update_each_pending/', views.update_each_pending, name='update_each_pending'),
    path('search/', views.search, name='search'),
    path('search_on/', views.search_on, name='search_on'),
    path('contact_us/', views.contact_us, name='contact_us'),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='activities/registration/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='activities/registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='activities/registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='activities/registration/password_reset_complete.html'),name='password_reset_complete'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)