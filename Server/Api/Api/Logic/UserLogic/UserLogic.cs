using Models;

namespace Api.Logic.UserLogic
{
    public class UserLogic
    {
        public User GetUserByLoginAndPassword(string login, string password)
        {
            using (var context = ApplicationContextGetter.GetContext())
            {
                var user = context.Users.FirstOrDefault(x => x.UserName == login && x.Password == password);
                if (user == null)
                    throw new Exception("Error #1 Cannot find user given creditionals");
                return user;
            }
        }
    }
}
