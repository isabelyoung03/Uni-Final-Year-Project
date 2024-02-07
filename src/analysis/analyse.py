import csv
import os
from src.environment.Goal_factory import GoalFactory


class Analysis:
    def analyse(maze, player):
        search_algorithm = player.get_search_algorithm()
        algorithm_enum_value = search_algorithm.get_enum().value

        results_folder = "results"
        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        filename = os.path.join(results_folder, algorithm_enum_value + "_" + maze.get_maze_size().to_string() + "_results.csv")

        with open(filename, mode='w', newline='') as csv_file:
            fields = ['Goal Location', 'Moves Taken']
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()

            player_location = player.get_location()
            goals = GoalFactory.generate_goals_in_all_cells(maze)

            for goal in goals:
                search_algorithm.set_goal(goal)
                path = search_algorithm.search(player_location[0], player_location[1], [])
                writer.writerow({'Goal Location': goal.get_location(), 'Moves Taken': len(path)})

        print(f"Analysis results saved to '{filename}'")

