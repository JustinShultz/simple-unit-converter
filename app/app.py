# Developed by @JustinShultz using Ladybug Tools. 
# You should have received a copy of the GNU Affero General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>

"""
Streamlit app for unit conversion.
"""

import streamlit as st
import pandas as pd

try:
    import ladybug.datatype
except ImportError as e:
    raise ImportError('\nFailed to import ladybug.datatype')

st.set_page_config(
    page_title="Unit Converter",
    layout='wide'
)

st.markdown("# Simple Unit Converter")

# all_u = [': '.join([key, ', '.join(val)]) for key, val in ladybug.datatype.UNITS.items()]

all_type = [''.join(key) for key in ladybug.datatype.UNITS]
# st.write(type(all_type))
# all_type.sort()
# st.write(type(all_type))
u_type = st.selectbox(
    "What do you want to convert?",
    sorted(all_type),
    index=3,
)

type_units = [''.join(val) for val in ladybug.datatype.UNITS[u_type]]
unit = st.selectbox(
    "Starting unit",
    type_units
)

value = st.number_input(
    'Starting value',
    value=1.0,
)
value = [value]

st.write('You are converting', value[0], unit)

st.markdown("## Converted Values")
for u in type_units:
    base_type = ladybug.datatype.TYPESDICT[u_type]()
    if u == unit:
        continue
    else:
        # st.write('base_type: ', base_type, 'value: ', value, '\nu: ', u, '\nunit: ', unit)
        converted_value = base_type.to_unit(
            values=value, 
            unit=u, 
            from_unit=unit)
        st.write(u,":",converted_value[0])