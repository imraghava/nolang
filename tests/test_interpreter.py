
from support import BaseTest, reformat_code
from nolang.interpreter import Interpreter
from nolang.compiler import compile_module
from nolang.frameobject import Frame
from nolang.objects.space import Space

class TestInterpreterBasic(BaseTest):
    def setup_method(self, meth):
        self.space = Space(None)

    def interpret(self, code):
        interpreter = Interpreter()
        bytecode = self.compile(code)
        bytecode.setup(self.space)
        f = Frame(bytecode)
        return interpreter.interpret(self.space, bytecode, f)

    def test_interpret(self):
        w_res = self.interpret('''
            var x;
            x = 1;
            ''')
        assert w_res is self.space.w_None

    def test_var_assign(self):
        w_res = self.interpret('''
            var x;
            x = 3;
            return x;
        ''')
        assert self.space.int_w(w_res) == 3

    def test_while_loop(self):
        w_r = self.interpret('''
            var i, s;
            i = 0;
            s = 0;
            while i < 10 {
                i = i + 1;
                s = s + i;
            }
            return s;
            ''')
        assert self.space.int_w(w_r) == 55

class TestInterpreter(BaseTest):
    def interpret(self, code):
        interpreter = Interpreter()
        source = reformat_code(code)
        ast = self.parse(source)
        w_mod = compile_module(source, ast)
        self.space = Space(interpreter)
        w_mod.initialize(self.space)
        return self.space.call_method(w_mod, 'main', [])

    def test_basic(self):
        w_res = self.interpret('''
            function main() {
                return 3;
            }
            ''')
        assert self.space.int_w(w_res) == 3

    def test_function_declaration_and_call(self):
        w_res = self.interpret('''
            function foo() {
                return 3;
            }

            function main() {
                return foo() + 1;
            }
            ''')
        assert self.space.int_w(w_res) == 4
