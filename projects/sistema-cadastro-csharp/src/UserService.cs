using System;
using System.Collections.Generic;
using System.Linq;

namespace SistemaCadastro;

public class UserService
{
    private readonly List<User> _users = new();
    private int _nextId = 1;

    public void AddUser(string name)
    {
        _users.Add(new User
        {
            Id = _nextId++,
            Name = name
        });
    }

    public IReadOnlyList<User> ListUsers()
    {
        return _users;
    }

    public bool RemoveUser(int id)
    {
        var user = _users.FirstOrDefault(item => item.Id == id);

        if (user is null)
        {
            return false;
        }

        return _users.Remove(user);
    }
}
