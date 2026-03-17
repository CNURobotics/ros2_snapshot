# Copyright 2026 Christopher Newport University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import shutil


def test_import_ros2_snapshot_core():
    import ros2_snapshot.core
    assert ros2_snapshot.core is not None


def test_import_ros2_snapshot_snapshot_pkg():
    import ros2_snapshot.snapshot
    assert ros2_snapshot.snapshot is not None


def test_import_ros2_snapshot_workspace_pkg():
    import ros2_snapshot.workspace_modeler
    assert ros2_snapshot.workspace_modeler is not None


def test_snapshot_entrypoint_import():
    from ros2_snapshot.snapshot.snapshot import main
    assert callable(main)


def test_workspace_entrypoint_import():
    from ros2_snapshot.workspace_modeler.workspace_modeler import main
    assert callable(main)


def test_graphviz_python_dependency():
    from graphviz import Digraph
    assert Digraph is not None


def test_graphviz_binary_dependency():
    assert shutil.which("dot") is not None