select count(*) as contact_count from ext_contacts where ext_contact_id in (3,4,5,6,24)
select REMOTE_READY,REMOTE_WORK,REMOTE_DONE from EXT_LOCAL_DIR_ACCESS where ext_contact_id in (24)