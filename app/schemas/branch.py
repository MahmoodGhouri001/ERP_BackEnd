from app import ma
class branchSchema(ma.Schema):
    class Meta:
        fields = ('branch_id','branch_name','branch_city','branch_state','branch_country','branch_status')

branch_schema = branchSchema()
branchs_schema = branchSchema(many=True)