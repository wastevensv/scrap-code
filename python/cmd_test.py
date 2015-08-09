import cmd

class add_cmd(cmd.Cmd,object):
    def preloop(self):
        print 'Hello'
        self.prompt = "(math)"
        super(add_cmd,self).preloop()
    def postloop(self):
        print 'Goodbye'
        super(add_cmd,self).postloop()
    def emptyline(self):
        print '*** empty line'
    def default(self,s):
        print '*** {} is not valid'.format(s)

    def do_add(self,s):
        l = s.split()
        t = 0
        try:
            for i in l:
               t += int(i)
        except ValueError:
           print "*** arguments should be numbers"
           return
        print t
    def help_add(self):
        print "descr: adds all numbers together"
        print "usage: add var1...varN"


    def do_exit(self,s):
        return True

interpreter = add_cmd()
interpreter.cmdloop()
