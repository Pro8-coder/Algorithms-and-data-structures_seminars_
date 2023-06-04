package hm.lesson4;

import java.util.*;

public class Tree<T extends Comparable<T>> {

    private class Node {
        T value;
        Node left;
        Node right;

        Node(T value) {
            this.value = value;
        }
    }

    private Node root;

    public boolean add(T value) {
        if (root == null) {
            root = new Node(value);
            return true;
        }

        return addNode(root, value);
    }

    private boolean addNode(Node current, T value) {
        if (value.compareTo(current.value) == 0) {
            return false;
        } else if (value.compareTo(current.value) < 0) {
            if (current.left == null) {
                current.left = new Node(value);
                return true;
            } else {
                return addNode(current.left, value);
            }
        } else {
            if (current.right == null) {
                current.right = new Node(value);
                return true;
            } else {
                return addNode(current.right, value);
            }
        }
    }

    public boolean contains(T value) {
        return findNode(root, value) != null;
    }

    private Node findNode(Node current, T value) {
        if (current == null) {
            return null;
        }

        if (value.compareTo(current.value) == 0) {
            return current;
        } else if (value.compareTo(current.value) < 0) {
            return findNode(current.left, value);
        } else {
            return findNode(current.right, value);
        }
    }

    public void remove(T value) {
        root = removeNode(root, value);
    }

    private Node removeNode(Node current, T value) {
        if (current == null) {
            return null;
        }

        if (value.compareTo(current.value) < 0) {
            current.left = removeNode(current.left, value);
            return current;
        } else if (value.compareTo(current.value) > 0) {
            current.right = removeNode(current.right, value);
            return current;
        }

        if (current.left == null && current.right == null) {
            return null;
        }

        if (current.left == null && current.right != null) {
            return current.right;
        }
        if (current.left != null && current.right == null) {
            return current.left;
        }

        Node smallestNodeOnTheRight = findFirst(current.right);
        T smallestValueOnTheRight = smallestNodeOnTheRight.value;
        current.value = smallestValueOnTheRight;
        current.right = removeNode(current.right, smallestValueOnTheRight);
        return current;
    }

    public T findFirst() {
        if (root == null) {
            throw new NoSuchElementException();
        }
        return findFirst(root).value;
    }

    private Node findFirst(Node current) {
        if (current.left == null) {
            return current;
        }
        return findFirst(current.left);
    }

    public List<T> dfs() {
        if (root == null) {
            return List.of();
        }

        List<T> list = new ArrayList<>();
        dfs(root, list);
        return list;
    }

    private void dfs(Node current, List<T> result) {
        if (current.left != null) {
            dfs(current.left, result);
        }
        result.add(current.value);
        if (current.right != null) {
            dfs(current.right, result);
        }
    }

    public List<T> bfs() {
        if (root == null) {
            return List.of();
        }

        List<T> result = new ArrayList<>();
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node next = queue.poll();
            result.add(next.value);

            if (next.left != null) {
                queue.add(next.left);
            }
            if (next.right != null) {
                queue.add(next.right);
            }
        }
        return result;
    }
}