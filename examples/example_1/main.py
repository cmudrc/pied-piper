from piperabm.model.samples import model_2 as model
from piperabm.actions.move.track import Track
from piperabm.actions.move.tracks import Tracks
from piperabm.actions.move import Move
from piperabm.time import Date, DeltaTime
from piperabm.society.agent.samples import agent_0
from piperabm.graphics import Animation


""" Setup model """
model.current_date = Date(2000, 1, 1)
model.set_step_size(DeltaTime(minutes=1))


""" Create move action """
pos_start = [-60, 40]
pos_end = [200, 20]
infrastructure = model.infrastructure
nodes = infrastructure.all_nodes(type='settlement')
index_start, _ = infrastructure.find_nearest_node(pos_start, items=nodes)
index_end, _ = infrastructure.find_nearest_node(pos_end, items=nodes)
path = infrastructure.find_path(index_start, index_end)
tracks = Tracks()
for i, index in enumerate(path):
    if i != 0:
        node_start = infrastructure.get(path[i-1])
        pos_start = node_start.pos
        node_end = infrastructure.get(path[i])
        pos_end = node_end.pos
        track = Track(pos_start, pos_end)
        tracks.add(track)
#tracks.print

date_start = Date(2000, 1, 1)
move = Move(
    transportation=agent_0.transportation,
    date_start=date_start
)
move.add_tracks(tracks)
#move.print


""" Add agent to model """
agent_0.home = index_start
model.add(agent_0)


""" Add move action to agent within model """
agents = model.all_agents
agent = model.get(agents[0])
agent.queue.add(move)


""" Run model """
animation = Animation()
#agent.resources.print
for i in range(3):
    model.run(1)
    #agent.resources.print
    #ag.print
    fig = model.fig()
    animation.add_figure(fig)

animation.render()
    #date = date_start + DeltaTime(minutes=3)
    #result = move.update(date)
    #print(move.current_progress)
