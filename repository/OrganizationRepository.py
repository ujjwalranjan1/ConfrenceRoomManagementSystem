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
        try:
            return self.organization_by_id[oid]
        except:
            print("no organization exist")

    def get_organization_by_name(self,name):
        try:
            return self.organization_by_name[name]
        except:
            print("no such organization exist")

    def get_all_organization(self):
        return self.organization_by_id.values()