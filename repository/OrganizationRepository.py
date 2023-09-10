from entity.Organization import Organization

class OrganizationRepository:
    def __init__(self):
        self.organization_by_id={}
        self.organization_by_name={}

    def create_organization(self,**kwargs):
        organization=Organization(**kwargs)
        self.organization_by_id[organization.get_oid()]=organization
        self.organization_by_name[organization.get_name()]=organization

    def delete_organization_by_id(self,oid):
        organization=self.organization_by_id[oid]
        self.organization_by_id.pop(oid)
        self.organization_by_name.pop(organization.get_name())

    def delete_organization_by_name(self,name):
        organization=self.organization_by_name[name]
        self.organization_by_id.pop(organization.get_oid())
        self.organization_by_name.pop(name)

    def get_organization_by_id(self,oid):
        return self.organization_by_id[oid]

    def get_organization_by_name(self,name):
        return self.organization_by_name[name]

    def get_all_organization_id(self):
        return self.organization_by_id.values()