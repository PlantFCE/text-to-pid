from config import graph

num_successful_tests = 0
num_tests = 0

def test(query):
    global num_tests, num_successful_tests
    num_tests += 1
    data = graph.query(query).data()
    if data and len(data) > 0:
            return "❌ Failed"
    num_successful_tests += 1
    return "✅ Passed"

print("Rule 1: Pumps must have outlet pressure gauges...      ", end="")
print(test("""
MATCH (p)-[:FLOWS_TO]->(x)
WHERE p.type CONTAINS 'Pump'
  AND NOT (x)<-[:MEASURES]-(:Instrument {type:'PressureGauge'})
RETURN p.id AS Pump, x.id AS Outlet
"""))

print("Rule 2: Control valves must be controlled by a loop... ", end="")
print(test("""
MATCH (v:Valve)
WHERE v.type CONTAINS 'Control'
  AND NOT (v)<-[:CONTROLS]-(:ControlLoop)
RETURN v.id AS UncontrolledValve
"""))

print("========================================================================")

if (num_successful_tests == num_tests):
      print(f"✅ All {num_tests} tests passed.")
else:
      print(f"❌ {num_successful_tests}/{num_tests} tests passed.")