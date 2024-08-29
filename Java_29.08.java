package com.datorium.Datorium.API.Repo;

import com.datorium.Datorium.API.DTOs.User;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class UserRepo {

    private final ArrayList<User> users = new ArrayList<>();
    private static final String url ="jdbc:sqlite:/Users/lindariekstina/Downloads/Datorium-API/Users.db";

    public int add(User user) {
        try (Connection conn = DriverManager.getConnection(url)) {
            if (conn != null) {
                Statement statement = conn.createStatement();
                statement.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(20))");
                statement.execute("INSERT INTO people (name) values ('" + user.name + "')");
            }
            return 1; // to show successful adding
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
        return 0; // to show unsuccessful adding
    }

    public List<User> getAllUsers() {
        return users;
    }

    public User updateUser(int userIndex, User updateUserDTO) {
        var user = users.get(userIndex);
        user.setName(updateUserDTO.getName());
        return user;
    }
}

