from config import organization_repository,user_service
from entity.Organization import Organization

class OrganizationService:

    def add_organization(self,org_name,**kwargs):
        organization_repository.create_organization(
            org_name=org_name,
            **kwargs
        )
    
    def delete_organization(self,org_name):
        org=organization_repository.get_organization_by_name(org_name)
        employee_ids=org.get_employee_id()
        for emp_id in employee_ids:
            user_service.delete_user(emp_id)
        organization_repository.delete_organization_by_name(org_name)
            
        


    def add_user_in_organization(self,organization_id,user_id):
        organization=organization_repository.get_organization_by_id(organization_id)
        organization.add_employee(user_id)
    
    def remove_user_in_organization(self,org_id,user_id):
        organization=organization_repository.get_organization_by_id(org_id)
        organization.delete_employee(user_id)
    
    def get_all_organization(self):
        return organization_repository.get_all_organization_id()