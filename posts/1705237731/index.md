# 测试页面

# [返回](/)

# 关于

此**页面**是~~用来~~^^测试^^功能[^1]的

[^1]: 脚注测试

![图标](/favicon.ico)

![img](https://github.com/cueavyqwp/cueavyqwp.github.io/assets/127200270/5e7ea25d-b594-40f8-b3a3-64b47e0beab6)

---

# H1
## H2
### H3
#### H4
##### H5
###### H6

> 1
> 2
> 3
> > 4
> > 5
> 6

LaTeX:

$$
\begin{gather*}
\begin{matrix} 0 & 1 \\ 1 & 0 \end{matrix}\quad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\\
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\quad
\begin{Bmatrix} 1 & 0 \\ 0 & -1 \end{Bmatrix}\\
\begin{vmatrix} a & b \\ c & d \end{vmatrix}\quad
\begin{Vmatrix} i & 0 \\ 0 & -i \end{Vmatrix}
\end{gather*}
$$

$$
\begin{array}{*{20}{l}}
{{}_{ }^{ } \int _{ }^{ }k \text{d} x=kx+C}\\
{{}_{ }^{ } \int _{ }^{ }\mathop{{x}}\nolimits^{{ \mu }} \text{d} x=\frac{{\mathop{{x}}\nolimits^{{ \mu +1}}}}{{ \mu +1}}+C,{ \left( { \mu  \neq -1} \right) }}\\
{{}_{ }^{ } \int _{ }^{ }\frac{{1}}{{x}} \text{d} x= \text{ln} { \left| {x} \right| }+C}\\
{{}_{ }^{ } \int _{ }^{ }\frac{{1}}{{1+\mathop{{x}}\nolimits^{{2}}}} \text{d} x= \text{arctan} x+C}\\
{{}_{ }^{ } \int _{ }^{ }\frac{{1}}{{\sqrt{{1-\mathop{{x}}\nolimits^{{2}}}}}} \text{d} x= \text{arcsin} x+C}
\end{array}
$$

$$
\overrightarrow{P_0P} \ \underrightarrow{P_0P} \ \overline{P_0P}
$$

```python
"""
renderer
"""
import pygments.formatters
import pygments.lexers
import traceback
import pygments
import mistune
import bs4

__all__ = [ "HTMLRenderer" ]

class HTMLRenderer( mistune.HTMLRenderer ) :

    def block_code( self, code : str , info : str | None = None ) -> str :
        try :
            assert isinstance( info , str )
            lexer = pygments.lexers.get_lexer_by_name( info )
            formatter = pygments.formatters.HtmlFormatter()
            return pygments.highlight( code , lexer , formatter )
        except Exception :
            traceback.print_exc()
            return f"\n<pre><code>{ code }</code></pre>"

    def heading( self , *args , **kwargs ) -> str :
        ret = super().heading( *args , **kwargs )
        soup = bs4.BeautifulSoup( ret , "html.parser" )
        head = soup.find( f"h{ kwargs[ 'level' ] }" )
        head[ "id" ] = head.text
        return soup.prettify( "utf-8" ).decode()
```
