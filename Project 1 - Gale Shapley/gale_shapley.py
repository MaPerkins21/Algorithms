def gale_shapley(positions, interns):
    """
    Implements the Gale-Shapley stable matching algorithm using only 2D arrays.
    """

    num_positions = len(positions)
    num_interns = len(interns)

    # List of unmatched positions
    unmatched_positions = list(range(num_positions))

    # Tracks which intern each position will propose to next
    next_intern = [0] * num_positions

    # Stores which position each intern is currently matched with (-1 = unmatched)
    matching = [-1] * num_interns

    # Stores which intern each position is matched with (-1 = unmatched)
    position_matches = [-1] * num_positions

    # Create ranking matrix for interns
    # rank[i][p] = k means intern i ranks position p with priority k (lower is better)
    rank = [[0] * num_positions for _ in range(num_interns)]
    for i in range(num_interns):
        for k, p in enumerate(interns[i]):
            rank[i][p] = k

    # Main Gale-Shapley loop
    while unmatched_positions:
        p = unmatched_positions.pop(0)

        if next_intern[p] >= len(positions[p]):
            continue  # No more interns to propose to

        # Propose to the next intern on position p's preference list
        i = positions[p][next_intern[p]]
        next_intern[p] += 1

        if matching[i] == -1:
            # Intern is free, accept the proposal
            matching[i] = p
            position_matches[p] = i
        else:
            current_p = matching[i]
            if rank[i][p] < rank[i][current_p]:
                # Intern prefers the new position
                matching[i] = p
                position_matches[p] = i
                position_matches[current_p] = -1
                unmatched_positions.append(current_p)
            else:
                # Intern rejects the proposal
                unmatched_positions.append(p)

    return position_matches
