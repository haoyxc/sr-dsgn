from flask_restful import Api, Resource, reqparse
from flask import jsonify
from api.helpers.FormParams import FormParams
from api.helpers.Schedule import Schedule

class FormHandler(Resource):
  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'message': "Form Api Handler"
      }

  def post(self):
    print(self)
    parser = reqparse.RequestParser()
    print(parser)
    parser.add_argument('type', type=str)
    parser.add_argument('message', type=str)

    # Add arguments
    parser.add_argument('tankInitial')
    parser.add_argument('tankCapacity')
    parser.add_argument('turnover')
    parser.add_argument('butylDemand')
    parser.add_argument('butylCapacity')
    parser.add_argument('butylDensity')
    parser.add_argument('butylProd')
    parser.add_argument('ethylDemand')
    parser.add_argument('ethylCapacity')
    parser.add_argument('ethylDensity')
    parser.add_argument('ethylProd')

    args = parser.parse_args()

    print(args)
    # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

    request_type = args['type']
    request_json = args['message']

    # Get the arguments 
    req_tank_initial = args['tankInitial']
    req_tank_capacity = args['tankCapacity']
    req_turnover = args['turnover']
    req_butyl_demand = args['butylDemand']
    req_butyl_capacity = args['butylCapacity']
    req_butyl_density = args['butylDensity']
    req_butyl_prod = args['butylProd']
    req_ethyl_demand = args['ethylDemand']
    req_ethyl_capacity = args['ethylCapacity']
    req_ethyl_density = args['ethylDensity']
    req_ethyl_prod = args['ethylProd']

    # print(req_tank_initial, req_tank_capacity, req_downtime, req_butyl_demand, req_butyl_capacity, req_butyl_density, req_butyl_prod, req_ethyl_demand, req_ethyl_capacity, req_ethyl_density, req_ethyl_prod)

    fp = FormParams(float(req_tank_initial), float(req_tank_capacity), float(req_turnover), float(req_butyl_demand), float(req_butyl_capacity), float(req_butyl_density), float(req_butyl_prod), float(req_ethyl_demand), float(req_ethyl_capacity), float(req_ethyl_density), float(req_ethyl_prod))
    # ret_status, ret_msg = ReturnData(request_type, request_json)
    # currently just returning the req straight

    schedObj : Schedule = fp.randomlyAssignSchedule(5)
    print(schedObj.getSchedule())
    print("total production: ", schedObj.getTotalProduction())
    
    ret_status = request_type
    ret_msg = request_json


    if ret_msg:
      message = "Your Message Requested: {}".format(ret_msg)
    else:
      message = "No Msg"
    
    final_ret = {"status": "Success", "message": message, "schedule": schedObj.getSchedule(), "totalProduction": schedObj.getTotalProduction()}
    return final_ret