delete_ability_query = """DELETE FROM ability_types
                    LEFT JOIN abilities
                    ON ability_types.id = abilities.hero_id
                    WHERE abilities.hero_id = %s"""