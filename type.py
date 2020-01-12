import enum

from treewalker import TreeWalker

class Type(enum.Enum):
    """Type is used to describe identifier's type"""
    
    # Built-in types
    INT = 0
    FLOAT = 1
    BOOL = 2
    STRING = 3

class TypeChecker(TreeWalker):
    def visit_ident(self, ident):
        pass
    
    def visit_const(self, const):
        pass
    
    def visit_relop(self, relop):
        pass
    
    def visit_addop(self, addop):
        pass
    
    def visit_op(self, op):
        pass
    
    def visit_uop(self, uop):
        pass
    
    def visit_decl(self, decl):
        pass
    
    def visit_assign(self, assign):
        pass
    
    def visit_inc(self, inc):
        pass
    
    def visit_dec(self, dec):
        pass
    
    def visit_if(self, if_):
        pass
    
    def visit_while(self, while_):
        pass
    
    def visit_for(self, for_):
        pass
    
    def visit_dowhile(self, dowhile):
        pass
    
    def visit_break(self, break_):
        pass
    
    def visit_cont(self, cont):
        pass
    
    def visit_expr(self, expr):
        pass
    
    def visit_print(self, print_):
        pass
    
    def visit_blk(self, blk):
        pass
    
    def visit_prgm(self, prgm):
        pass